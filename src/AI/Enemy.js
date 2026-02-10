/**
 * 🎮 ThreeJSEvolution - AI Enemy System
 * 敌人AI系统：巡逻、追逐、攻击、状态机
 */

class Enemy {
    constructor(options = {}) {
        this.id = options.id || 'enemy_' + Date.now();
        this.type = options.type || 'melee'; // melee, ranged, boss
        this.position = options.position || new THREE.Vector3(0, 1, 0);
        this.mesh = null;
        this.health = options.health || 100;
        this.maxHealth = this.health;
        this.speed = options.speed || 3;
        this.damage = options.damage || 10;
        this.detectionRange = options.detectionRange || 15;
        this.attackRange = options.attackRange || 2;
        this.attackCooldown = options.attackCooldown || 1000;
        this.lastAttackTime = 0;
        
        // AI State Machine
        this.state = 'IDLE'; // IDLE, PATROL, CHASE, ATTACK, FLEE, DEAD
        this.stateMachine = {
            'IDLE': this.updateIdle.bind(this),
            'PATROL': this.updatePatrol.bind(this),
            'CHASE': this.updateChase.bind(this),
            'ATTACK': this.updateAttack.bind(this),
            'FLEE': this.updateFlee.bind(this),
            'DEAD': this.updateDead.bind(this)
        };
        
        // Patrol settings
        this.patrolPoints = options.patrolPoints || [];
        this.patrolIndex = 0;
        this.patrolWaitTime = 0;
        this.patrolSpeed = this.speed * 0.5;
        
        // Target
        this.target = null;
        this.lastSeenPosition = new THREE.Vector3();
        
        // Visual feedback
        this.healthBar = null;
        this.damageFlash = 0;
    }
    
    createMesh(scene) {
        // 根据敌人类型创建不同外观
        const geometry = new THREE.BoxGeometry(1, 1.5, 1);
        
        let color;
        switch(this.type) {
            case 'ranged': color = 0xff4444; break; // 红色远程敌人
            case 'boss': color = 0x880088; break; // 紫色BOSS
            default: color = 0xff8800; // 橙色近战敌人
        }
        
        const material = new THREE.MeshPhongMaterial({ color: color });
        this.mesh = new THREE.Mesh(geometry, material);
        this.mesh.position.copy(this.position);
        this.mesh.castShadow = true;
        
        // 添加眼睛（表示方向）
        const eyeGeo = new THREE.SphereGeometry(0.15, 8, 8);
        const eyeMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
        
        const leftEye = new THREE.Mesh(eyeGeo, eyeMat);
        leftEye.position.set(-0.2, 0.3, 0.5);
        this.mesh.add(leftEye);
        
        const rightEye = new THREE.Mesh(eyeGeo, eyeMat);
        rightEye.position.set(0.2, 0.3, 0.5);
        this.mesh.add(rightEye);
        
        // 添加血条
        this.createHealthBar(scene);
        
        scene.add(this.mesh);
        return this.mesh;
    }
    
    createHealthBar(scene) {
        const canvas = document.createElement('canvas');
        canvas.width = 64;
        canvas.height = 8;
        this.healthBarTexture = canvas;
        
        const texture = new THREE.CanvasTexture(canvas);
        const material = new THREE.SpriteMaterial({ map: texture, transparent: true });
        this.healthBar = new THREE.Sprite(material);
        this.healthBar.scale.set(1.5, 0.2, 1);
        this.healthBar.position.set(0, 1.2, 0);
        this.mesh.add(this.healthBar);
        
        this.updateHealthBar();
    }
    
    updateHealthBar() {
        if (!this.healthBarTexture) return;
        
        const ctx = this.healthBarTexture.getContext('2d');
        const healthPercent = this.health / this.maxHealth;
        
        // 背景
        ctx.fillStyle = '#333333';
        ctx.fillRect(0, 0, 64, 8);
        
        // 血条
        const color = healthPercent > 0.5 ? '#00ff00' : healthPercent > 0.25 ? '#ffff00' : '#ff0000';
        ctx.fillStyle = color;
        ctx.fillRect(1, 1, 62 * healthPercent, 6);
        
        if (this.healthBarTexture) {
            this.healthBarTexture.needsUpdate = true;
        }
    }
    
    // AI State Updates
    updateIdle(deltaTime, gameState) {
        this.mesh.rotation.y += deltaTime * 0.5;
        
        // 检测玩家
        if (this.target && this.distanceTo(this.target) < this.detectionRange) {
            this.state = 'CHASE';
        }
        
        // 开始巡逻
        if (this.patrolPoints.length > 0) {
            this.state = 'PATROL';
        }
    }
    
    updatePatrol(deltaTime, gameState) {
        if (this.patrolPoints.length === 0) {
            this.state = 'IDLE';
            return;
        }
        
        const targetPoint = this.patrolPoints[this.patrolIndex];
        const distance = this.distanceTo(targetPoint);
        
        if (distance < 0.5) {
            // 到达巡逻点，等待
            this.patrolWaitTime -= deltaTime;
            if (this.patrolWaitTime <= 0) {
                this.patrolIndex = (this.patrolIndex + 1) % this.patrolPoints.length;
                this.patrolWaitTime = 2;
            }
        } else {
            // 移动到巡逻点
            this.moveTo(targetPoint, this.patrolSpeed * deltaTime);
        }
        
        // 检测玩家
        if (this.target && this.distanceTo(this.target) < this.detectionRange) {
            this.state = 'CHASE';
        }
    }
    
    updateChase(deltaTime, gameState) {
        if (!this.target) {
            this.state = 'IDLE';
            return;
        }
        
        const distance = this.distanceTo(this.target);
        
        if (distance < this.attackRange) {
            this.state = 'ATTACK';
        } else if (distance > this.detectionRange * 1.5) {
            // 丢失目标
            this.state = 'PATROL';
        } else {
            // 追逐
            this.moveTo(this.target, this.speed * deltaTime);
            this.lookAt(this.target);
        }
    }
    
    updateAttack(deltaTime, gameState) {
        const now = Date.now();
        if (now - this.lastAttackTime > this.attackCooldown) {
            this.attack(gameState);
            this.lastAttackTime = now;
        }
        
        // 攻击后返回追逐
        this.state = 'CHASE';
    }
    
    updateFlee(deltaTime, gameState) {
        // 逃向远离玩家的方向
        if (this.target) {
            const fleeDir = new THREE.Vector3().subVectors(this.position, this.target.position).normalize();
            const fleeTarget = new THREE.Vector3().addVectors(this.position, fleeDir.multiplyScalar(10));
            this.moveTo(fleeTarget, this.speed * 0.8 * deltaTime);
        }
    }
    
    updateDead(deltaTime, gameState) {
        // 死亡动画已结束
    }
    
    // Actions
    moveTo(target, speed) {
        const direction = new THREE.Vector3().subVectors(target, this.position);
        direction.y = 0; // 保持水平移动
        direction.normalize();
        
        this.position.add(direction.multiplyScalar(speed));
        this.mesh.position.copy(this.position);
        this.lookAt(target);
    }
    
    lookAt(target) {
        this.mesh.lookAt(target.x, this.mesh.position.y, target.z);
    }
    
    distanceTo(target) {
        return this.position.distanceTo(target);
    }
    
    attack(gameState) {
        // 攻击动画效果
        this.mesh.scale.set(1.2, 0.8, 1.2);
        setTimeout(() => {
            if (this.mesh) this.mesh.scale.set(1, 1, 1);
        }, 150);
        
        // 对玩家造成伤害
        if (gameState.player && this.distanceTo(gameState.player.position) < this.attackRange + 1) {
            gameState.player.takeDamage?.(this.damage);
        }
        
        // 远程敌人发射子弹
        if (this.type === 'ranged') {
            this.shootProjectile(gameState);
        }
    }
    
    shootProjectile(gameState) {
        if (!gameState.projectiles) return;
        
        const projectile = {
            position: this.position.clone(),
            direction: new THREE.Vector3().subVectors(gameState.player.position, this.position).normalize(),
            speed: 10,
            damage: this.damage * 0.5,
            life: 3,
            color: 0xff0000
        };
        
        gameState.projectiles.push(projectile);
    }
    
    takeDamage(amount) {
        this.health -= amount;
        this.updateHealthBar();
        
        // 受伤闪烁效果
        this.damageFlash = 1;
        if (this.mesh) {
            this.mesh.material.emissive.setHex(0xff0000);
        }
        
        if (this.health <= 0) {
            this.die();
        }
    }
    
    die() {
        this.state = 'DEAD';
        
        // 死亡效果
        if (this.mesh) {
            this.mesh.material.color.setHex(0x333333);
            this.mesh.rotation.x = Math.PI / 2;
            this.mesh.position.y = 0.25;
        }
        
        // 移除血条
        if (this.healthBar) {
            this.mesh.remove(this.healthBar);
        }
    }
    
    // Main update loop
    update(deltaTime, gameState) {
        // 更新受伤闪烁
        if (this.damageFlash > 0) {
            this.damageFlash -= deltaTime * 3;
            if (this.mesh && this.damageFlash > 0) {
                this.mesh.material.emissive.setHex(
                    new THREE.Color(0xff0000).multiplyScalar(this.damageFlash)
                );
            } else if (this.mesh) {
                this.mesh.material.emissive.setHex(0x000000);
            }
        }
        
        // 执行状态机
        const updateFn = this.stateMachine[this.state];
        if (updateFn) {
            updateFn(deltaTime, gameState);
        }
    }
    
    setTarget(entity) {
        this.target = entity;
    }
    
    addPatrolPoint(point) {
        this.patrolPoints.push(point.clone());
    }
}

// Enemy Spawner - 生成不同类型的敌人
class EnemySpawner {
    constructor(scene) {
        this.scene = scene;
        this.enemies = [];
        this.spawnPoints = [];
    }
    
    addSpawnPoint(x, y, z) {
        this.spawnPoints.push(new THREE.Vector3(x, y, z));
    }
    
    spawnEnemy(type = 'melee') {
        if (this.spawnPoints.length === 0) return null;
        
        const spawnPoint = this.spawnPoints[Math.floor(Math.random() * this.spawnPoints.length)];
        
        const enemy = new Enemy({
            type: type,
            position: spawnPoint.clone()
        });
        
        enemy.createMesh(this.scene);
        this.enemies.push(enemy);
        
        return enemy;
    }
    
    spawnWave(waveConfig) {
        const { melee = 3, ranged = 2, boss = false } = waveConfig;
        
        for (let i = 0; i < melee; i++) {
            this.spawnEnemy('melee');
        }
        
        for (let i = 0; i < ranged; i++) {
            this.spawnEnemy('ranged');
        }
        
        if (boss) {
            const bossEnemy = this.spawnEnemy('boss');
            bossEnemy.health = 500;
            bossEnemy.maxHealth = 500;
            bossEnemy.damage = 30;
            bossEnemy.speed = 2;
            bossEnemy.detectionRange = 25;
        }
    }
    
    update(deltaTime, gameState) {
        this.enemies.forEach(enemy => {
            enemy.update(deltaTime, gameState);
        });
        
        // 清理死亡敌人
        this.enemies = this.enemies.filter(enemy => enemy.state !== 'DEAD' || 
            (Date.now() - enemy.lastAttackTime < 5000));
    }
    
    getEnemies() {
        return this.enemies;
    }
    
    clear() {
        this.enemies.forEach(enemy => {
            if (enemy.mesh) {
                this.scene.remove(enemy.mesh);
            }
        });
        this.enemies = [];
    }
}

// 导出
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { Enemy, EnemySpawner };
}
