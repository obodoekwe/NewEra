document.addEventListener('DOMContentLoaded', () => {
  const statusBtn = document.getElementById('fetch-status');
  const statusOut = document.getElementById('status-output');
  const echoForm = document.getElementById('echo-form');
  const echoOut = document.getElementById('echo-output');

  if (statusBtn && statusOut) {
    statusBtn.addEventListener('click', async () => {
      const res = await fetch('/status');
      const data = await res.json();
      statusOut.textContent = JSON.stringify(data, null, 2);
    });
  }

  if (echoForm && echoOut) {
    echoForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const form = new FormData(e.currentTarget);
      const msg = form.get('msg') || '';
      const res = await fetch(`/echo?msg=${encodeURIComponent(msg)}`);
      const data = await res.json();
      echoOut.textContent = JSON.stringify(data, null, 2);
    });
  }
});
