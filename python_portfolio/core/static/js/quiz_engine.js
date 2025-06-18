let currentQuestion = 0,
    score = 0,
    userAnswers = [],
    timerInterval,
    quizQuestions = [];

// Load one question at a time
function loadQuestion() {
  const q = quizQuestions[currentQuestion];
  const qBox = document.getElementById('quizBox');

  const progress = ((currentQuestion + 1) / quizQuestions.length) * 100;
  document.getElementById('quizSummary').innerHTML = `
    <div class="progress mb-2">
      <div class="progress-bar bg-info" style="width: ${progress}%">${Math.round(progress)}%</div>
    </div>
    <p class="text-muted">Progress: ${currentQuestion + 1}/${quizQuestions.length} | <span id='timerDisplay'>⏱️ 15s</span></p>
  `;

  let html = `<h5><strong>Q${currentQuestion + 1}:</strong> ${q.question}</h5><form id="quizForm">`;

  q.options.forEach((opt, idx) => {
    html += `
      <div class="form-check">
        <input class="form-check-input" type="radio" name="answer" id="q${currentQuestion}_opt${idx}" value="${opt}">
        <label class="form-check-label" for="q${currentQuestion}_opt${idx}">${opt}</label>
      </div>`;
  });

  html += `
    <button type="button" class="btn btn-primary mt-3" onclick="submitAnswer()">Submit</button>
    <button type="button" class="btn btn-warning mt-3 ms-2" onclick="showHint()">💡 Hint</button>
    <div id="hintBox" class="mt-2 text-muted"></div>
  </form>`;

  qBox.innerHTML = html;
  setTimeout(startTimer, 50);
  document.getElementById("quizForm").addEventListener("submit", e => e.preventDefault());
}

function showHint() {
  const q = quizQuestions[currentQuestion];
  document.getElementById("hintBox").innerText = "Hint: " + (q.hint || "No hint available.");
}

function startTimer() {
  let timeLeft = 15;
  const timerDisplay = document.getElementById("timerDisplay");
  clearInterval(timerInterval);
  timerDisplay.classList.remove("text-danger");

  timerInterval = setInterval(() => {
    timeLeft--;
    timerDisplay.innerText = `⏱️ ${timeLeft}s`;

    if (timeLeft <= 5) timerDisplay.classList.add("text-danger");

    if (timeLeft <= 0) {
      clearInterval(timerInterval);
      timerDisplay.innerText = "⏱️ Time's up!";
      document.getElementById("quizBox").innerHTML += `
        <div class="alert alert-warning mt-3">⏱️ You ran out of time!</div>
        <button class="btn btn-primary" onclick="restartQuiz()">Restart</button>
      `;
    }
  }, 1000);
}

function submitAnswer() {
  clearInterval(timerInterval);
  const selected = document.querySelector('input[name="answer"]:checked');
  const q = quizQuestions[currentQuestion];
  const qBox = document.getElementById('quizBox');

  if (!selected) {
    alert("Please select an answer.");
    return;
  }

  const userAnswer = selected.value;
  const isCorrect = userAnswer === q.answer;

  userAnswers.push({
    question: q.question,
    selected: userAnswer,
    correct: q.answer,
    result: isCorrect ? '✅ Correct' : '❌ Incorrect'
  });

  const sound = document.getElementById(isCorrect ? "correctSound" : "wrongSound");
  if (sound) {
    sound.volume = 0.2;
    sound.play();
  }

  document.querySelectorAll('input[name="answer"]').forEach(input => {
    const label = input.nextElementSibling;
    if (input.value === q.answer) label.classList.add('text-success');
    if (input.checked && input.value !== q.answer) label.classList.add('text-danger');
    input.disabled = true;
  });

  qBox.innerHTML += `
    <div class="alert ${isCorrect ? 'alert-success' : 'alert-danger'} mt-3">
      ${isCorrect ? '✅ Correct!' : '❌ Wrong!'}<br>
      <strong>Correct Answer:</strong> ${q.answer}
    </div>
    <button class="btn btn-success" onclick="nextQuestion()">Next</button>
    <button class="btn btn-outline-primary ms-2" onclick="restartQuiz()">Restart</button>
  `;

  if (isCorrect) score++;
}

function nextQuestion() {
  currentQuestion++;
  if (currentQuestion < quizQuestions.length) {
    loadQuestion();
  } else {
    showFinalScore();
  }
}

function showFinalScore() {
  let message = score === quizQuestions.length ? "🎉 Perfect Score!" :
                score >= 7 ? "👍 Great job!" :
                "📘 Review and try again!";
  let result = `
    <h4 class="text-success">Quiz Complete!</h4>
    <p>You got <strong>${score}/${quizQuestions.length}</strong> correct. ${message}</p>
    <h5 class="mt-4">🧾 Review:</h5>
    <ul class="list-group">`;

  userAnswers.forEach((item, i) => {
    result += `
      <li class="list-group-item">
        <strong>Q${i + 1}:</strong> ${item.question}<br>
        <span class="${item.result.includes('✅') ? 'text-success' : 'text-danger'}">${item.result}</span><br>
        <strong>Your Answer:</strong> ${item.selected}<br>
        <strong>Correct:</strong> ${item.correct}
      </li>`;
  });

  result += `</ul>
    <button class="btn btn-primary mt-4" onclick="restartQuiz()">Start Again</button>
  `;

  document.getElementById('quizBox').innerHTML = result;
  document.getElementById('quizSummary').innerHTML = '';
}

function restartQuiz() {
  currentQuestion = 0;
  score = 0;
  userAnswers = [];
  loadQuestion();
}

// ✅ Load from quiz_questions.json based on topic key
function loadQuizData(topicKey) {
  fetch("/static/data/quiz_questions.json")
    .then(response => response.json())
    .then(data => {
      quizQuestions = data[topicKey] || [];
      currentQuestion = 0;
      score = 0;
      userAnswers = [];

      // ✅ Update quiz count badge after loading
      const quizCount = quizQuestions.length;
      const quizCountEl = document.getElementById("quizCount");
      const quizCountTextEl = document.getElementById("quizCountText");
      if (quizCountEl) quizCountEl.textContent = quizCount;
      if (quizCountTextEl) quizCountTextEl.textContent = quizCount;

      loadQuestion();
    })
    .catch(error => {
      console.error("Failed to load quiz data:", error);
      alert("🚫 Error loading quiz data.");
    });
}

// ✅ Wait for DOM to be ready
document.addEventListener("DOMContentLoaded", () => {
  // Load quiz data when quiz tab is shown
  const quizTab = document.querySelector('#quiz-tab');
  if (quizTab) {
    quizTab.addEventListener('shown.bs.tab', () => {
      if (quizQuestions.length === 0) {
        loadQuizData("numbers");  // ✅ Correct call to load quiz data
      } else {
        loadQuestion();  // In case it's already loaded
      }
    });
  }

  // Example count
  const exampleCards = document.querySelectorAll("#exampleCards .col").length;
  const exampleCountEl = document.getElementById("exampleCount");
  if (exampleCountEl) exampleCountEl.textContent = exampleCards;
});

