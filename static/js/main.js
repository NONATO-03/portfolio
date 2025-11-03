document.addEventListener('DOMContentLoaded', function() {

    // ANIMAÇÃO AO ROLAR A PÁGINA (Scroll) - anima toda vez que entra/sai da tela
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                entry.target.classList.remove('visible');
            }
        });
    }, {
        threshold: 0.1 // A animação começa quando 10% do elemento está visível
    });

    const elementsToAnimate = document.querySelectorAll('.animate-on-scroll');
    elementsToAnimate.forEach(element => {
        observer.observe(element);
    });

    // Lógica para ativar a seção atual ao rolar a página
    window.addEventListener('scroll', function() {
        const sections = document.querySelectorAll('.section');
        let scrollY = window.scrollY + window.innerHeight / 2;
        sections.forEach(section => {
            const rect = section.getBoundingClientRect();
            const top = rect.top + window.scrollY;
            const bottom = top + section.offsetHeight;
            if (scrollY >= top && scrollY < bottom) {
                sections.forEach(s => s.classList.remove('active-section'));
                section.classList.add('active-section');
            }
        });
    });

    // Gaveta de linguagens
    const floatingFrame = document.getElementById('floating-frame');
    const frameLanguages = document.getElementById('frame-languages');
    const languageIcons = frameLanguages.querySelectorAll('.language-icon');

    // --- Efeito automático de abrir/fechar gaveta ---
    let drawerAnimationFrame = null;
    let autoDrawerActive = false;
    let autoDrawerTimeout = null;

    function syncLanguagesDrawerPosition() {
        const floatingFrameRect = floatingFrame.getBoundingClientRect();
        const parentRect = floatingFrame.parentElement.getBoundingClientRect();
        const offsetTop = floatingFrameRect.top - parentRect.top;
        frameLanguages.style.transform = `translateY(${offsetTop}px)`;
    }
    function animateDrawerFollow() {
        if (frameLanguages.classList.contains('open')) {
            syncLanguagesDrawerPosition();
            drawerAnimationFrame = requestAnimationFrame(animateDrawerFollow);
        }
    }

    function openDrawer(auto = false) {
        if (auto) autoDrawerActive = true;
        frameLanguages.classList.add('open');
        updateLanguagesDrawer();
        animateDrawerFollow();
    }
    function closeDrawer(auto = false) {
        frameLanguages.classList.remove('open');
        if (drawerAnimationFrame) {
            cancelAnimationFrame(drawerAnimationFrame);
            drawerAnimationFrame = null;
        }
        if (auto) autoDrawerActive = false;
    }

    // Efeito automático: a cada 20s, abre por 10s e bloqueia hover durante esse tempo
    function startAutoDrawer() {
        function autoCycle() {
            openDrawer(true);
            autoDrawerTimeout = setTimeout(() => {
                closeDrawer(true);
                setTimeout(autoCycle, 10000); // espera 10s fechado, depois abre de novo
            }, 10000); // 10s aberto
        }
        autoCycle();
    }
    startAutoDrawer();

    // Abre gaveta ao passar mouse sobre frame vertical (só se não está no modo auto)
    floatingFrame.addEventListener('mouseenter', () => {
        if (!autoDrawerActive) {
            openDrawer();
        }
    });
    floatingFrame.addEventListener('mouseleave', () => {
        if (!autoDrawerActive) {
            closeDrawer();
        }
    });

    // Função para atualizar largura/altura da gaveta
    function updateLanguagesDrawer() {
        const activeIcons = frameLanguages.querySelectorAll('.language-icon.active');
        const total = activeIcons.length;
        const iconsPerCol = 5; // Máximo de ícones por coluna
        const colWidth = 66;   // largura de cada coluna (ícone + gap)
        const minWidth = 90;   // largura mínima do frame
        const iconHeight = 66; // altura de cada ícone + gap
        const padding = 36;

        // Calcula quantas colunas são necessárias
        let cols = Math.ceil(total / iconsPerCol);
        let width = Math.max(minWidth, cols * colWidth + padding);

        // Pega a altura real do frame vertical
        const floatingFrameRect = floatingFrame.getBoundingClientRect();
        const floatingFrameHeight = floatingFrameRect.height;

        // Calcula a altura necessária para os ícones (máximo: altura do frame vertical)
        let rows = Math.min(iconsPerCol, total);
        let neededHeight = rows * iconHeight + 36; // 36 = padding (18px em cima e embaixo)
        let height = Math.max(floatingFrameHeight, neededHeight);

        // Seta altura igual ao frame vertical OU suficiente para os ícones, o que for maior
        frameLanguages.style.setProperty('--frame-languages-width', width + 'px');
        frameLanguages.style.setProperty('--frame-languages-height', height + 'px');

        // Layout dos ícones: grid, máximo 5 por coluna
        const container = frameLanguages.querySelector('.languages-icons');
        container.style.display = 'grid';
        container.style.gridTemplateColumns = `repeat(${cols}, 1fr)`;
        container.style.gridAutoRows = `${iconHeight}px`;
        container.style.gap = '18px';
        container.style.height = '100%';
        container.style.alignItems = 'start';

        // Sincroniza a posição vertical da gaveta
        syncLanguagesDrawerPosition();
    }

    // Ativação/desativação dos ícones
    languageIcons.forEach(icon => {
        icon.classList.add('active');
        icon.addEventListener('click', function() {
            if (icon.classList.contains('active')) {
                icon.classList.remove('active');
                icon.classList.add('inactive');
            } else {
                icon.classList.remove('inactive');
                icon.classList.add('active');
            }
            updateLanguagesDrawer();
        });
    });

    // Atualiza altura e posição da gaveta ao redimensionar janela
    window.addEventListener('resize', updateLanguagesDrawer);

    updateLanguagesDrawer();
});