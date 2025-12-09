document.addEventListener('DOMContentLoaded', () => {
    console.log(">>> SISTEMA INICIADO.");

    // --- LÓGICA DE PESQUISA ---
    const searchInput = document.querySelector('.search-txt');
    const cards = document.querySelectorAll('.card');
    const noResultsMsg = document.getElementById('no-results');

    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            const searchValue = e.target.value.toLowerCase();
            let hasResults = false;

            if(searchValue.length > 0) {
                showScreen('home-screen');
            }

            cards.forEach(card => {
                const cardName = card.getAttribute('data-name');
                if (cardName.includes(searchValue)) {
                    card.style.display = "flex"; 
                    hasResults = true;
                } else {
                    card.style.display = "none";
                }
            });

            if (noResultsMsg) {
                noResultsMsg.style.display = hasResults ? "none" : "block";
            }
        });
    }

    // --- MODO ESCURO ---
    const themeBtn = document.getElementById('theme-toggle');
    const body = document.body;

    if (localStorage.getItem('theme') === 'dark') {
        body.classList.add('dark-mode');
        themeBtn.textContent = '☀️';
    }

    themeBtn.onclick = () => {
        body.classList.toggle('dark-mode');
        if (body.classList.contains('dark-mode')) {
            themeBtn.textContent = '☀️';
            localStorage.setItem('theme', 'dark');
        } else {
            themeBtn.textContent = '🌙';
            localStorage.setItem('theme', 'light');
        }
    }

    // RESTO DO CÓDIGO (JOGO, MODAIS, ETC)
    const correctAudio = document.getElementById('correct-sound');
    const incorrectAudio = document.getElementById('incorrect-sound');

    const database = {
        html: [
            { q: "O que significa HTML?", options: ["HyperText Markup Language", "Home Tool Markup Language", "Hyperlinks and Text Markup"], answer: 0 },
            { q: "Qual tag cria o maior título?", options: ["<h6>", "<h1>", "<head>"], answer: 1 },
            { q: "Qual tag cria uma quebra de linha?", options: ["<lb>", "<break>", "<br>"], answer: 2 },
            { q: "Onde colocamos o título da aba?", options: ["<body>", "<title>", "<head>"], answer: 1 },
            { q: "Qual atributo define o texto alternativo da imagem?", options: ["title", "longdesc", "alt"], answer: 2 }
        ],
        css: [
            { q: "O que significa CSS?", options: ["Creative Style Sheets", "Cascading Style Sheets", "Computer Style Sheets"], answer: 1 },
            { q: "Qual propriedade muda a cor de fundo?", options: ["bgcolor", "color", "background-color"], answer: 2 },
            { q: "Como comentar em CSS?", options: ["// comentário", "/* comentário */", "' comentário"], answer: 1 },
            { q: "Qual propriedade muda o tamanho da fonte?", options: ["font-size", "text-size", "text-style"], answer: 0 },
            { q: "Como selecionar um ID chamado 'demo'?", options: [".demo", "#demo", "*demo"], answer: 1 }
        ],
        js: [
            { q: "Dentro de qual elemento HTML colocamos JS?", options: ["<script>", "<js>", "<javascript>"], answer: 0 },
            { q: "Como exibir um alerta?", options: ["msg('Olá')", "alertBox('Olá')", "alert('Olá')"], answer: 2 },
            { q: "Como criar uma função?", options: ["function:myFunc()", "function myFunc()", "create myFunc()"], answer: 1 },
            { q: "Como chamar uma função 'myFunc'?", options: ["call myFunc()", "myFunc()", "call function myFunc()"], answer: 1 },
            { q: "Qual operador atribui valor?", options: ["-", "*", "="], answer: 2 }
        ]
    };

    const screens = {
        'home-screen': document.getElementById('home-screen'),
        'quiz-screen': document.getElementById('quiz-screen'),
        'result-screen': document.getElementById('result-screen')
    };

    const ui = {
        categoryBadge: document.getElementById('category-badge'),
        scoreDisplay: document.getElementById('score-display'),
        questionText: document.getElementById('question-text'),
        optionsContainer: document.getElementById('options-container'),
        questionCounter: document.getElementById('question-counter'),
        nextBtn: document.getElementById('next-btn'),
        progressFill: document.getElementById('progress-fill'),
        finalScore: document.getElementById('final-score'),
        totalQuestions: document.getElementById('total-questions'),
        progressValue: document.querySelector('.progress-value'),
        progressCircle: document.querySelector('.progress-ring__circle')
    };

    let currentQuestions = [];
    let currentQuestionIndex = 0;
    let score = 0;

    function resetBackground() {
        document.body.classList.remove('correct-bg');
        document.body.classList.remove('incorrect-bg');
    }

    window.showScreen = function(screenName) {
        resetBackground();
        Object.values(screens).forEach(screen => {
            if(screen) screen.classList.remove('active');
        });
        const target = screens[screenName];
        if (target) target.classList.add('active');
    }

    window.startGame = function(category) {
        if (!database[category]) return;
        currentQuestions = database[category];
        currentQuestionIndex = 0;
        score = 0;
        if(ui.categoryBadge) ui.categoryBadge.textContent = category.toUpperCase();
        showScreen('quiz-screen'); 
        loadQuestion();
    }

    function loadQuestion() {
        resetBackground();
        const q = currentQuestions[currentQuestionIndex];
        
        ui.questionText.textContent = `${currentQuestionIndex + 1}. ${q.q}`;
        ui.scoreDisplay.textContent = `Score: ${score}`;
        ui.questionCounter.textContent = `${currentQuestionIndex + 1} / ${currentQuestions.length}`;
        
        const percent = ((currentQuestionIndex) / currentQuestions.length) * 100;
        ui.progressFill.style.width = `${percent}%`;

        ui.optionsContainer.innerHTML = '';
        ui.nextBtn.disabled = true;
        ui.nextBtn.textContent = "Escolha uma opção";

        q.options.forEach((opt, index) => {
            const btn = document.createElement('button');
            btn.className = 'option';
            btn.textContent = opt;
            btn.onclick = () => checkAnswer(btn, index);
            ui.optionsContainer.appendChild(btn);
        });
    }

    function checkAnswer(btn, index) {
        const correct = currentQuestions[currentQuestionIndex].answer;
        const options = ui.optionsContainer.children;

        if (index === correct) {
            score++;
            btn.classList.add('correct');
            document.body.classList.add('correct-bg');
            if(correctAudio) correctAudio.play();
        } else {
            btn.classList.add('incorrect');
            options[correct].classList.add('correct');
            document.body.classList.add('incorrect-bg');
            if(incorrectAudio) incorrectAudio.play();
        }

        for(let opt of options) {
            opt.classList.add('disabled');
            opt.onclick = null;
        }

        ui.nextBtn.disabled = false;
        ui.nextBtn.textContent = "Próxima →";
    }

    if(ui.nextBtn) {
        ui.nextBtn.onclick = () => {
            if (currentQuestionIndex < currentQuestions.length - 1) {
                currentQuestionIndex++;
                loadQuestion();
            } else {
                finishGame();
            }
        };
    }

    function finishGame() {
        resetBackground();
        ui.finalScore.textContent = score;
        ui.totalQuestions.textContent = currentQuestions.length;
        ui.progressFill.style.width = '100%';
        
        const total = currentQuestions.length;
        const percentage = Math.round((score / total) * 100);
        ui.progressValue.textContent = `${percentage}%`;

        const radius = 70;
        const circumference = 2 * Math.PI * radius;
        const offset = circumference - (percentage / 100) * circumference;

        if(ui.progressCircle) {
            ui.progressCircle.style.strokeDasharray = `${circumference} ${circumference}`;
            ui.progressCircle.style.strokeDashoffset = offset;
        }
        showScreen('result-screen');
    }

    const restartBtn = document.getElementById('restart-btn');
    if(restartBtn) restartBtn.onclick = () => showScreen('home-screen');
    const homeBtn = document.getElementById('home-btn');
    if(homeBtn) homeBtn.onclick = () => showScreen('home-screen');

    // MODAIS
    const openBtns = document.querySelectorAll('.open-modal');
    const closeBtns = document.querySelectorAll('.close-modal');
    const actionBtns = document.querySelectorAll('.close-modal-action');
    const overlays = document.querySelectorAll('.modal-overlay');

    openBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const id = btn.getAttribute('data-modal');
            const modal = document.getElementById(id);
            if(modal) modal.classList.add('active');
        });
    });

    closeBtns.forEach(btn => {
        btn.onclick = () => btn.closest('.modal-overlay').classList.remove('active');
    });

    actionBtns.forEach(btn => {
        btn.onclick = () => btn.closest('.modal-overlay').classList.remove('active');
    });

    overlays.forEach(overlay => {
        overlay.onclick = (e) => {
            if(e.target === overlay) overlay.classList.remove('active');
        }
    });
});