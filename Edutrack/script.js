const form = document.getElementById('reminder-form');
const input = document.getElementById('reminder-input');
const list = document.getElementById('reminder-list');
const showBtn = document.getElementById('show-reminder-btn');
const hideBtn = document.getElementById('hide-reminder-btn');
const container = document.querySelector('.container');
const badge = document.getElementById('reminder-badge');

// Load reminders from localStorage on page load
let reminders = JSON.parse(localStorage.getItem('reminders')) || [];

function saveReminders() {
  localStorage.setItem('reminders', JSON.stringify(reminders));
}

function updateBadge() {
  badge.textContent = reminders.length;
  badge.style.display = reminders.length > 0 ? 'inline-block' : 'none';
}

function renderReminders() {
  list.innerHTML = '';
  reminders.forEach((reminder, index) => {
    const li = document.createElement('li');
    li.textContent = reminder;

    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = '✖';
    deleteBtn.classList.add('delete-btn');
    deleteBtn.onclick = () => {
      reminders.splice(index, 1);
      saveReminders();
      renderReminders();
    };

    li.appendChild(deleteBtn);
    list.appendChild(li);
  });
  updateBadge();
}

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const text = input.value.trim();
  if (text) {
    reminders.push(text);
    saveReminders();
    renderReminders();
    input.value = '';
  }
  updateBadge();
});

showBtn.addEventListener('click', function() {
  container.style.display = 'block';
  showBtn.style.display = 'none';
  updateBadge();
});

hideBtn.addEventListener('click', function() {
  container.style.display = 'none';
  showBtn.style.display = 'inline-block';
  updateBadge();
});

// Initial badge update
updateBadge();

renderReminders();
