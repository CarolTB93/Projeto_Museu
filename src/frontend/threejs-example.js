// Tour Virtual do Museu com Three.js
// Para rodar, inclua <script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script> no HTML

document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('threejs-demo');
    if (!container) return;
    
    if (typeof THREE === 'undefined') {
        container.innerHTML = '<p>Three.js não carregado. <br><br>Para ativar o tour virtual, adicione este script ao HTML:<br><code>&lt;script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"&gt;&lt;/script&gt;</code></p>';
        return;
    }
    
    // Configuração inicial
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    
    renderer.setSize(container.clientWidth, container.clientHeight);
    renderer.setClearColor(0x87CEEB); // Cor de fundo azul céu
    container.appendChild(renderer.domElement);
    
    // Iluminação
    const ambientLight = new THREE.AmbientLight(0x404040, 0.6);
    scene.add(ambientLight);
    
    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
    directionalLight.position.set(10, 10, 5);
    scene.add(directionalLight);
    
    // Criar ambiente do museu
    createMuseumEnvironment();
    
    // Posição inicial da câmera
    camera.position.set(0, 2, 8);
    camera.lookAt(0, 0, 0);
    
    // Controles básicos com mouse
    let mouseX = 0, mouseY = 0;
    let targetX = 0, targetY = 0;
    
    document.addEventListener('mousemove', onMouseMove, false);
    
    function onMouseMove(event) {
        mouseX = (event.clientX - window.innerWidth / 2) / 100;
        mouseY = (event.clientY - window.innerHeight / 2) / 100;
    }
    
    function createMuseumEnvironment() {
        // Chão do museu
        const floorGeometry = new THREE.PlaneGeometry(20, 20);
        const floorMaterial = new THREE.MeshLambertMaterial({ color: 0x8B7355 });
        const floor = new THREE.Mesh(floorGeometry, floorMaterial);
        floor.rotation.x = -Math.PI / 2;
        scene.add(floor);
        
        // Paredes
        const wallMaterial = new THREE.MeshLambertMaterial({ color: 0xF5F5DC });
        
        // Parede de trás
        const backWallGeometry = new THREE.PlaneGeometry(20, 8);
        const backWall = new THREE.Mesh(backWallGeometry, wallMaterial);
        backWall.position.z = -10;
        backWall.position.y = 4;
        scene.add(backWall);
        
        // Paredes laterais
        const sideWallGeometry = new THREE.PlaneGeometry(20, 8);
        const leftWall = new THREE.Mesh(sideWallGeometry, wallMaterial);
        leftWall.rotation.y = Math.PI / 2;
        leftWall.position.x = -10;
        leftWall.position.y = 4;
        scene.add(leftWall);
        
        const rightWall = new THREE.Mesh(sideWallGeometry, wallMaterial);
        rightWall.rotation.y = -Math.PI / 2;
        rightWall.position.x = 10;
        rightWall.position.y = 4;
        scene.add(rightWall);
        
        // Adicionar algumas "exposições" simples
        createExhibits();
    }
    
    function createExhibits() {
        // Pedestal central com um "avião" simples
        const pedestalGeometry = new THREE.CylinderGeometry(1.5, 1.5, 1);
        const pedestalMaterial = new THREE.MeshLambertMaterial({ color: 0x696969 });
        const pedestal = new THREE.Mesh(pedestalGeometry, pedestalMaterial);
        pedestal.position.y = 0.5;
        scene.add(pedestal);
        
        // "Avião" simplificado
        const airplaneGroup = new THREE.Group();
        
        // Fuselagem
        const fuselageGeometry = new THREE.CylinderGeometry(0.1, 0.15, 2);
        const fuselageMaterial = new THREE.MeshLambertMaterial({ color: 0x0066CC });
        const fuselage = new THREE.Mesh(fuselageGeometry, fuselageMaterial);
        fuselage.rotation.z = Math.PI / 2;
        airplaneGroup.add(fuselage);
        
        // Asas
        const wingGeometry = new THREE.BoxGeometry(1.5, 0.05, 0.3);
        const wingMaterial = new THREE.MeshLambertMaterial({ color: 0x0066CC });
        const wings = new THREE.Mesh(wingGeometry, wingMaterial);
        airplaneGroup.add(wings);
        
        airplaneGroup.position.y = 2;
        airplaneGroup.rotation.y = Math.PI / 4;
        scene.add(airplaneGroup);
        
        // Alguns painéis informativos nas paredes
        createInfoPanels();
    }
    
    function createInfoPanels() {
        const panelGeometry = new THREE.PlaneGeometry(2, 1.5);
        const panelMaterial = new THREE.MeshLambertMaterial({ color: 0xFFFFFF });
        
        for (let i = 0; i < 3; i++) {
            const panel = new THREE.Mesh(panelGeometry, panelMaterial);
            panel.position.set(-9.5, 2, -5 + i * 5);
            panel.rotation.y = Math.PI / 2;
            scene.add(panel);
        }
    }
    
    // Animação
    function animate() {
        requestAnimationFrame(animate);
        
        // Movimento suave da câmera baseado no mouse
        targetX = mouseX * 0.001;
        targetY = mouseY * 0.001;
        
        camera.rotation.x += 0.05 * (targetY - camera.rotation.x);
        camera.rotation.y += 0.05 * (targetX - camera.rotation.y);
        
        renderer.render(scene, camera);
    }
    
    // Responsividade
    function onWindowResize() {
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
    }
    
    window.addEventListener('resize', onWindowResize, false);
    
    animate();
});
