(function () {
  'use strict';
  var el = function (id) { return document.getElementById('bug-report-' + id); };
  var dialog = el('dialog');
  if (!dialog) return;
  var screenshot = null, previewUrl = null, busy = false, sent = false, reportId;
  function newId() {
    if (crypto.randomUUID) return crypto.randomUUID();
    return '10000000-1000-4000-8000-100000000000'.replace(/[018]/g, function(c) {
      return (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16);
    });
  }
  function status(message) { el('status').textContent = message; }
  function clearImage() {
    if (previewUrl) URL.revokeObjectURL(previewUrl);
    previewUrl = null; screenshot = null;
    el('preview').removeAttribute('src'); el('file').value = ''; el('attachment').hidden = true;
  }
  function attach(file) {
    if (busy || !file) return;
    if (!['image/png', 'image/jpeg', 'image/webp'].includes(file.type)) {
      status('Please choose a PNG, JPEG or WebP screenshot.'); return;
    }
    if (!file.size || file.size > 4 * 1024 * 1024) {
      status('Please choose a screenshot smaller than 4 MB.'); return;
    }
    clearImage(); screenshot = file; previewUrl = URL.createObjectURL(file);
    el('preview').src = previewUrl; el('filename').textContent = file.name || 'Screenshot';
    el('attachment').hidden = false; status('');
  }
  function close() { if (!busy) dialog.close(); }
  el('open').addEventListener('click', function () {
    if (sent) { el('form').reset(); clearImage(); sent = false; reportId = null; }
    if (!reportId) reportId = newId();
    el('form').hidden = false; el('success').hidden = true; status(''); dialog.showModal();
  });
  ['close', 'cancel', 'done'].forEach(function(id) { el(id).addEventListener('click', close); });
  dialog.addEventListener('cancel', function(e) { if (busy) e.preventDefault(); });
  dialog.addEventListener('click', function(e) {
    var r = dialog.getBoundingClientRect();
    if (e.target === dialog && (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom)) close();
  });
  el('remove').addEventListener('click', function() { clearImage(); status(''); });
  el('file').addEventListener('change', function() { attach(this.files[0]); });
  var upload = dialog.querySelector('.bug-report-upload');
  ['dragover', 'dragleave', 'drop'].forEach(function(type) {
    upload.addEventListener(type, function(e) {
      e.preventDefault(); upload.classList.toggle('dragging', type === 'dragover');
      if (type === 'drop') attach(e.dataTransfer.files[0]);
    });
  });
  dialog.addEventListener('paste', function(e) {
    var files = e.clipboardData && e.clipboardData.files;
    if (files && files.length) { e.preventDefault(); attach(files[0]); }
  });
  function imageContent(file) {
    return new Promise(function(resolve, reject) {
      var reader = new FileReader();
      reader.onload = function() { resolve(String(reader.result).split(',')[1]); };
      reader.onerror = reject; reader.readAsDataURL(file);
    });
  }
  el('form').addEventListener('submit', async function(e) {
    e.preventDefault(); if (busy || !this.reportValidity()) return;
    var report = {id: reportId, description: el('description').value.trim(), email: el('email').value.trim(),
      categories: Array.from(dialog.querySelectorAll('[name="bug-category"]:checked')).map(function(c) { return c.value; }), details: {}};
    if (el('details').checked) {
      var runtime = document.getElementById('cm-global-runtime');
      // Use the declared tab only. Never include the URL, query or hash: they can contain secrets.
      var active = document.querySelector('.left-nav-item.active[data-tab], .tab.active[data-tab]');
      report.details = {version: dialog.dataset.version || '', view: active ? active.dataset.tab : '',
        runtime: runtime ? runtime.value : '', browser: navigator.userAgent.slice(0, 300), hosting: window.CLOUD_MODE ? 'cloud' : 'local'};
    }
    busy = true; status('Sending your report…');
    el('fields').disabled = true; el('send').disabled = true; el('close').disabled = true; el('cancel').disabled = true;
    var controller = new AbortController(), timeout = setTimeout(function() { controller.abort(); }, 35000);
    try {
      if (screenshot) report.screenshot = {content: await imageContent(screenshot)};
      var response = await fetch('/api/support/bugs', {method: 'POST', headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(report), signal: controller.signal});
      var result = await response.json();
      if (!response.ok || result.ok !== true || result.id !== report.id) {
        var errors = {400: 'Please check your description, email and screenshot, then try again.',
          413: 'Please choose a screenshot smaller than 4 MB.', 429: 'You have sent several reports. Please wait a few minutes and try again.'};
        throw new Error(errors[response.status] || 'Your report could not be sent. Your draft is still here. Try again, or email vivek@clawmetry.com.');
      }
      sent = true; clearImage(); el('form').hidden = true; el('success').hidden = false; el('done').focus();
    } catch (error) {
      status(error.name === 'AbortError' ? 'Sending took too long. Your draft is still here. Please try again.' :
        (error.message && error.message.startsWith('Please ') || error.message && error.message.startsWith('You have ') || error.message && error.message.startsWith('Your report ') ? error.message : 'Your report could not be sent. Your draft is still here. Please try again.'));
    } finally {
      clearTimeout(timeout); busy = false;
      el('fields').disabled = false; el('send').disabled = false; el('close').disabled = false; el('cancel').disabled = false;
    }
  });
})();
