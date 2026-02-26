// ===== KEPAAR FM — JAVASCRIPT PRINCIPAL =====

// ===== LECTEUR EN DIRECT =====
let isPlaying = false, isMuted = false;
const audio = document.getElementById('radioAudio');
const playBtn = document.getElementById('playBtn');
const muteBtn = document.getElementById('muteBtn');
const playerStatus = document.getElementById('playerStatus');
const eqBars = document.getElementById('eqBars');

function togglePlay() {
  isPlaying = !isPlaying;
  if (isPlaying) {
    if (audio) audio.play().catch(() => {});
    if (playBtn) playBtn.innerHTML = '⏸';
    if (playerStatus) {
      playerStatus.innerHTML = '● En direct — Kepaar FM 99.7';
      playerStatus.style.color = 'var(--green-light)';
    }
    if (eqBars) eqBars.style.opacity = '1';
  } else {
    if (audio) audio.pause();
    if (playBtn) playBtn.innerHTML = '▶';
    if (playerStatus) {
      playerStatus.innerHTML = '● En pause';
      playerStatus.style.color = 'var(--text-muted)';
    }
    if (eqBars) eqBars.style.opacity = '0.3';
  }
}

function toggleMute() {
  isMuted = !isMuted;
  if (audio) audio.muted = isMuted;
  if (muteBtn) muteBtn.innerHTML = isMuted ? '🔇' : '🔊';
}

function setVolume(val) {
  if (audio) audio.volume = val / 100;
}

function shareRadio() {
  if (navigator.share) {
    navigator.share({
      title: 'Kepaar FM 99.7',
      text: 'Écoutez Kepaar FM 99.7 — Radio Islamique de Kaolack',
      url: window.location.href
    });
  } else {
    navigator.clipboard.writeText(window.location.href)
      .then(() => alert('Lien copié ! Partagez-le avec vos proches.'));
  }
}

// ===== LECTEURS AUDIO MINI (émissions archivées) =====
let currentMiniAudio = null;
let currentMiniBtn = null;
let progressInterval = null;

function playMini(id, btn) {
  const audioEl = document.getElementById('audio-' + id);
  const progEl = document.getElementById('prog-' + id);
  if (!audioEl) return;

  // Si on clique sur le même audio en cours
  if (currentMiniAudio === audioEl) {
    if (audioEl.paused) {
      audioEl.play();
      btn.innerHTML = '⏸';
    } else {
      audioEl.pause();
      btn.innerHTML = '▶';
    }
    return;
  }

  // Arrêter l'audio précédent
  if (currentMiniAudio) {
    currentMiniAudio.pause();
    currentMiniAudio.currentTime = 0;
    if (currentMiniBtn) currentMiniBtn.innerHTML = '▶';
    clearInterval(progressInterval);
    const oldId = currentMiniAudio.id.replace('audio-', '');
    const oldProg = document.getElementById('prog-' + oldId);
    if (oldProg) oldProg.style.width = '0%';
  }

  currentMiniAudio = audioEl;
  currentMiniBtn = btn;
  audioEl.play().catch(() => {});
  btn.innerHTML = '⏸';

  // Mise à jour de la barre de progression
  progressInterval = setInterval(() => {
    if (audioEl.duration && progEl) {
      const pct = (audioEl.currentTime / audioEl.duration) * 100;
      progEl.style.width = pct + '%';
    }
    if (audioEl.ended) {
      btn.innerHTML = '▶';
      if (progEl) progEl.style.width = '0%';
      currentMiniAudio = null;
      clearInterval(progressInterval);
    }
  }, 500);
}

function seekAudio(e, bar, id) {
  const audioEl = document.getElementById('audio-' + id);
  const progEl = document.getElementById('prog-' + id);
  if (!audioEl || !audioEl.duration) return;
  const pct = e.offsetX / bar.offsetWidth;
  audioEl.currentTime = pct * audioEl.duration;
  if (progEl) progEl.style.width = (pct * 100) + '%';
}

// ===== ANIMATION AU SCROLL =====
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.style.opacity = '1';
      e.target.style.transform = 'translateY(0)';
    }
  });
}, { threshold: 0.08 });

document.querySelectorAll('.news-card, .anim-card, .prog-item, .audio-card, .don-card, .stat-box').forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(18px)';
  el.style.transition = 'opacity 0.45s ease, transform 0.45s ease';
  observer.observe(el);
});