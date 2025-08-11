async function submitForm(e) {
  e.preventDefault();
  const html = document.querySelector('textarea[name="html"]').value;
  const res = await fetch('/api/evaluate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ html })
  });
  const data = await res.json();
  document.getElementById('result').innerText = JSON.stringify(data, null, 2);
  return false;
}
