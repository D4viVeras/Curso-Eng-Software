const startBtn = document.querySelector('.start-btn');
const popupInfo = document.querySelector('.popup-info'); // Popup do Guia
const exitBtn = document.querySelector('.exit-btn');
const main = document.querySelector('.main');
const continueBtn = document.querySelector('.continue-btn');
const quizSection = document.querySelector('.quiz-section');
const quizBox = document.querySelector('.quiz-box');
const resultBox = document.querySelector('.result-box');
const tryAgainBtn = document.querySelector('.tryAgain-btn');
const goHomeBtn = document.querySelector('.goHome-btn');
const homeSection = document.querySelector('.home');
const logo = document.querySelector('.logo');
const nextBtn = document.querySelector('.next-btn');
const optionList = document.querySelector('.option-list');

// Áudios
const correctAudio = document.getElementById('correct-sound');
const incorrectAudio = document.getElementById('incorrect-sound');

// Variáveis do Header (Links)
const navHome = document.querySelector('.nav-home');
const navAbout = document.querySelector('.nav-about');
const navServices = document.querySelector('.nav-services');
const navContact = document.querySelector('.nav-contact');

// Variáveis do Footer (Links)
const linkPrivacy = document.querySelector('.link-privacy');
const linkTerms = document.querySelector('.link-terms');
const linkContact = document.querySelector('.link-contact');

// Variáveis dos Popups
const popupHome = document.querySelector('.popup-home');
const popupAbout = document.querySelector('.popup-about');
const popupServices = document.querySelector('.popup-services');
const popupPrivacy = document.querySelector('.popup-privacy');
const popupTerms = document.querySelector('.popup-terms');
const popupContact = document.querySelector('.popup-contact');

// Botões de fechar popups (Genérico para todos)
const closePopupBtns = document.querySelectorAll('.close-popup-btn');

let questionCount = 0;
let questionNumb = 1;
let userScore = 0;

// --- LÓGICA PRINCIPAL ---

startBtn.onclick = () => {
    popupInfo.classList.add('active');
    main.classList.add('active');
}

exitBtn.onclick = () => {
    popupInfo.classList.remove('active');
    main.classList.remove('active');
}

continueBtn.onclick = () => {
    quizSection.classList.add('active');
    popupInfo.classList.remove('active');
    main.classList.remove('active');
    quizBox.classList.add('active');

    homeSection.style.display = 'none';

    showQuestions(0);
    questionCounter(1);
    headerScore();
}

tryAgainBtn.onclick = () => {
    quizBox.classList.add('active');
    nextBtn.classList.remove('active');
    resultBox.classList.remove('active');

    questionCount = 0;
    questionNumb = 1;
    userScore = 0;
    showQuestions(questionCount);
    questionCounter(questionNumb);
    headerScore();
}

// Botão de Pânico (Logo)
logo.onclick = () => {
    quizSection.classList.remove('active');
    popupInfo.classList.remove('active');
    resultBox.classList.remove('active');
    nextBtn.classList.remove('active');
    main.classList.remove('active');

    // Fecha TODOS os popups extras se estiverem abertos
    popupHome.classList.remove('active');
    popupAbout.classList.remove('active');
    popupServices.classList.remove('active');
    popupPrivacy.classList.remove('active');
    popupTerms.classList.remove('active');
    popupContact.classList.remove('active');

    homeSection.style.display = 'flex';

    document.body.classList.remove('correct-bg');
    document.body.classList.remove('incorrect-bg');

    questionCount = 0;
    questionNumb = 1;
    userScore = 0;
    showQuestions(questionCount);
    questionCounter(questionNumb);
    headerScore();
}

goHomeBtn.onclick = () => {
    quizSection.classList.remove('active');
    nextBtn.classList.remove('active');
    resultBox.classList.remove('active');

    homeSection.style.display = 'flex';

    document.body.classList.remove('correct-bg');
    document.body.classList.remove('incorrect-bg');

    questionCount = 0;
    questionNumb = 1;
    userScore = 0;
    showQuestions(questionCount);
    questionCounter(questionNumb);
    headerScore();
}

nextBtn.onclick = () => {
    if (questionCount < questions.length - 1) {
        document.body.classList.remove('correct-bg');
        document.body.classList.remove('incorrect-bg');

        questionCount++;
        questionNumb++;
        showQuestions(questionCount);
        questionCounter(questionNumb);

        nextBtn.classList.remove('active');
    }
    else {
        document.body.classList.remove('correct-bg');
        document.body.classList.remove('incorrect-bg');
        showResultBox();
    }
}

// --- LÓGICA DO HEADER (NAVBAR) ---

navHome.onclick = (e) => {
    e.preventDefault();
    popupHome.classList.add('active');
    main.classList.add('active');
}

navAbout.onclick = (e) => {
    e.preventDefault();
    popupAbout.classList.add('active');
    main.classList.add('active');
}

navServices.onclick = (e) => {
    e.preventDefault();
    popupServices.classList.add('active');
    main.classList.add('active');
}

navContact.onclick = (e) => {
    e.preventDefault();
    popupContact.classList.add('active'); // Reutiliza o popup de contato
    main.classList.add('active');
}


// --- LÓGICA DO FOOTER ---

linkPrivacy.onclick = (e) => {
    e.preventDefault();
    popupPrivacy.classList.add('active');
    main.classList.add('active');
}

linkTerms.onclick = (e) => {
    e.preventDefault();
    popupTerms.classList.add('active');
    main.classList.add('active');
}

linkContact.onclick = (e) => {
    e.preventDefault();
    popupContact.classList.add('active');
    main.classList.add('active');
}

// Função Genérica para fechar qualquer popup
closePopupBtns.forEach(btn => {
    btn.onclick = () => {
        popupHome.classList.remove('active');
        popupAbout.classList.remove('active');
        popupServices.classList.remove('active');
        popupPrivacy.classList.remove('active');
        popupTerms.classList.remove('active');
        popupContact.classList.remove('active');
        
        // Só remove o desfoque se o Quiz ou o Guia Inicial NÃO estiverem abertos
        // Isso evita bugs visuais se você abrir um popup "por cima" do jogo
        if (!quizSection.classList.contains('active') && !popupInfo.classList.contains('active')) {
            main.classList.remove('active');
        } else {
            // Se o quiz ou o guia estiverem abertos, apenas fecha o popup superior, mas mantém o blur
        }
        
        // Simplificação: Se quiser que feche o blur sempre (comportamento padrão simples):
        // main.classList.remove('active'); 
        // Mas o código acima é mais inteligente. Para manter simples como antes, use:
        if (!popupInfo.classList.contains('active')) { 
             main.classList.remove('active');
        }
    }
});


// --- FUNÇÕES AUXILIARES ---

function showQuestions(index) {
    const questionText = document.querySelector('.question-text');
    questionText.textContent = `${questions[index].numb}. ${questions[index].question}`;

    let optionTag = `<div class="option"><span>${questions[index].options[0]}</span></div>
        <div class="option"><span>${questions[index].options[1]}</span></div>
        <div class="option"><span>${questions[index].options[2]}</span></div>
        <div class="option"><span>${questions[index].options[3]}</span></div>`;

    optionList.innerHTML = optionTag;

    const option = document.querySelectorAll('.option');
    for (let i = 0; i < option.length; i++) {
        option[i].setAttribute('onclick', 'optionSelected(this)');
    }
}

function decodeHTML(text) {
    let txt = document.createElement("textarea");
    txt.innerHTML = text;
    return txt.value;
}

function optionSelected(answer) {
    let userAnswer = answer.textContent;
    let correctAnswer = decodeHTML(questions[questionCount].answer).trim();
    let allOptions = optionList.children.length;

    if (userAnswer == correctAnswer) {
        answer.classList.add('correct');
        userScore += 1;
        headerScore();
        document.body.classList.add('correct-bg');
        correctAudio.play();
    }
    else {
        answer.classList.add('incorrect');
        document.body.classList.add('incorrect-bg');
        incorrectAudio.play();

        for (let i = 0; i < allOptions; i++) {
            if (optionList.children[i].textContent == correctAnswer) {
                optionList.children[i].setAttribute('class', 'option correct');
            }
        }
    }

    for (let i = 0; i < allOptions; i++) {
        optionList.children[i].classList.add('disabled');
    }

    nextBtn.classList.add('active');
}

function questionCounter(index) {
    const questionTotal = document.querySelector('.question-total');
    questionTotal.textContent = `${index} de ${questions.length} Perguntas`;
}

function headerScore() {
    const headerScoreText = document.querySelector('.header-score');
    headerScoreText.textContent = `Score: ${userScore} / ${questions.length}`;
}

function showResultBox() {
    quizBox.classList.remove('active');
    resultBox.classList.add('active');

    const scoreText = document.querySelector('.score-text');
    scoreText.textContent = `Sua pontuação é ${userScore} de ${questions.length}`;

    const circularProgress = document.querySelector('.circular-progress');
    const progressValue = document.querySelector('.progress-value');
    let progressStartValue = -1;
    let progressEndValue = (userScore / questions.length) * 100;
    let speed = 20;

    let progress = setInterval(() => {
        progressStartValue++;
        progressValue.textContent = `${progressStartValue}%`;
        circularProgress.style.background = `conic-gradient(#000000 ${progressStartValue * 3.6}deg, #d4d3d4 ${progressStartValue * 3.6}deg)`;

        if (progressStartValue == progressEndValue) {
            clearInterval(progress);
        }
    }, speed);
}