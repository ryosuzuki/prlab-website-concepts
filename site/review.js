const filter = document.querySelector('#filter');
if (filter) {
  const choices = [...document.querySelectorAll('.select input')];
  const output = document.querySelector('#selection');
  const entries = [...document.querySelectorAll('.entry')];
  let saved = [];
  try { saved = JSON.parse(localStorage.getItem('prlab-shortlist') ?? '[]'); } catch {}
  choices.forEach(choice => { choice.checked = saved.includes(choice.value); });
  const selected = () => choices.filter(choice => choice.checked);
  function updateSelection() {
    const list = selected();
    try { localStorage.setItem('prlab-shortlist', JSON.stringify(list.map(item => item.value))); } catch {}
    output.textContent = list.length ? `${list.length} shortlisted · saved on this device` : 'No concepts shortlisted';
  }
  choices.forEach(choice => choice.addEventListener('change', updateSelection));
  updateSelection();
  filter.addEventListener('change', () => {
    entries.forEach(entry => { entry.hidden = filter.value !== 'All concepts' && entry.dataset.category !== filter.value; });
  });
  document.querySelector('#copy').addEventListener('click', async () => {
    const list = selected();
    if (!list.length) return;
    const lines = list.map(item => `${item.dataset.label} — ${new URL('concepts/' + item.value + '.html', location.href)}`);
    try {
      await navigator.clipboard.writeText(lines.join('\n'));
      output.textContent = 'Shortlist copied';
    } catch {
      output.textContent = list.map(item => item.dataset.label).join(', ');
    }
  });
}
document.querySelectorAll('.switch').forEach(group => {
  const buttons = [...group.querySelectorAll('button')];
  buttons.forEach(button => button.addEventListener('click', () => {
    buttons.forEach(item => {
      const active = item === button;
      item.setAttribute('aria-expanded', String(active));
      document.getElementById(item.getAttribute('aria-controls')).hidden = !active;
    });
  }));
});
const reveal = document.querySelector('.lens-intro input');
if (reveal) {
  reveal.addEventListener('input', () => document.querySelector('[data-reveal]').style.setProperty('--amount', reveal.value + '%'));
}
