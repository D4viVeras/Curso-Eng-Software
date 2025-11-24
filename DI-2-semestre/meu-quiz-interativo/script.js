const startBtn = document.querySelector('.start-btn')
const popupInfo = document.querySelector('.popup-info')
const exitBtn = document.querySelector('.exit-btn')
const main = document.querySelector('.main')
const continueBtn = document.querySelector('.continue-btn')
const quizSection = document.querySelector('.quiz-section')
const quizBox = document.querySelector('.quiz-box')
const resultBox = document.querySelector('.result-box')
const tryAgainBtn = document.querySelector('.tryAgain-btn')
const goHomeBtn = document.querySelector('.goHome-btn')
const homeSection = document.querySelector('.home')
const logo = document.querySelector('.logo')
const correctAudio = document.getElementById('correct-sound')
const incorrectAudio = document.getElementById('incorrect-sound')

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

logo.onclick = () => {
    quizSection.classList.remove('active');
    popupInfo.classList.remove('active');
    resultBox.classList.remove('active');
    nextBtn.classList.remove('active');
    main.classList.remove('active');

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

    questionCount = 0;
    questionNumb = 1;
    userScore = 0;
    showQuestions(questionCount);
    questionCounter(questionNumb);

    headerScore();

    document.body.classList.remove('correct-bg');
    document.body.classList.remove('incorrect-bg');

}

let questionCount = 0;
let questionNumb = 1;
let userScore = 0;

const nextBtn = document.querySelector('.next-btn');

nextBtn.onclick = () => {
    if (questionCount <questions.length -1) {
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

const optionList = document.querySelector('.option-list')

//getting questions and options from array
function  showQuestions(index) {
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


//código para fazer o decode do HTML,
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
        answer.classList.add('correct')
        userScore +=1;
        headerScore();
        document.body.classList.add('correct-bg');
        correctAudio.play();
    }
    else {
        answer.classList.add('incorrect')
        document.body.classList.add('incorrect-bg');
        incorrectAudio.play();

        for (let i = 0; i < allOptions; i++) {
            if (optionList.children[i].textContent == correctAnswer) {
                optionList.children[i].setAttribute('class', 'option correct')
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
    questionTotal.textContent = `${index} de ${questions.length} Perguntas`
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
    let progressEndValue= (userScore / questions.length) * 100;
    let speed = 20;

    let progress = setInterval(() => {
        progressStartValue++;
        progressValue.textContent = `${progressStartValue}%`
        circularProgress.style.background = `conic-gradient(#000000 ${progressStartValue * 3.6}deg, #d4d3d4 ${progressStartValue * 3.6}deg)`;

        if (progressStartValue == progressEndValue) {
            clearInterval(progress);
        }
    }, speed);
}