let preferences = JSON.parse(localStorage.getItem("preferences")) || {
  tech: 0,
  sports: 0,
  entertainment: 0
};

function trackClick(category) {
  preferences[category]++;
  localStorage.setItem("preferences", JSON.stringify(preferences));
  updateUI();
}

function getTopCategory() {
  return Object.keys(preferences).reduce((a, b) =>
    preferences[a] > preferences[b] ? a : b
  );
}

function updateUI() {
  let topCategory = getTopCategory();
  document.getElementById("recommendation").innerText =
    "Recommended: " + topCategory;
}

updateUI();
