async function fetchData(season) {
  const res = await fetch(`/api/players/league-leaders?season=${season}&stat=PTS`);
  return res.json();
}

function populateSeasons() {
  const select = document.getElementById('season');
  const seasons = [];
  for (let y = 2023; y >= 2015; y--) {
    const next = String(y + 1).slice(-2);
    seasons.push(`${y}-${next}`);
  }
  seasons.forEach(s => {
    const opt = document.createElement('option');
    opt.value = s; opt.textContent = s; select.appendChild(opt);
  });
  select.addEventListener('change', () => renderChart(select.value));
}

let chart;
async function renderChart(season) {
  const data = await fetchData(season);
  const labels = data.slice(0, 10).map(p => p.PLAYER);
  const values = data.slice(0, 10).map(p => p.PTS);
  const ctx = document.getElementById('chart').getContext('2d');
  if (chart) chart.destroy();
  chart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels,
      datasets: [{ label: `Points (${season})`, data: values, backgroundColor: 'rgba(54, 162, 235, 0.6)' }]
    },
    options: { responsive: true, scales: { y: { beginAtZero: true } } }
  });
}

populateSeasons();
renderChart('2023-24');
