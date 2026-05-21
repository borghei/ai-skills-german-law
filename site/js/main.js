/* ── Scroll Fade-in (gentle, opacity only) ───────────────────── */
const fadeObserver = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (e.isIntersecting) e.target.classList.add('visible');
  });
}, { threshold: 0.1 });
document.querySelectorAll('.fade-in').forEach((el) => fadeObserver.observe(el));

/* ── Counter Animation ───────────────────────────────────────── */
let countersDone = false;
const statsEl = document.getElementById('stats');
if (statsEl) {
  const counterObserver = new IntersectionObserver((entries) => {
    if (countersDone) return;
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      countersDone = true;
      document.querySelectorAll('.stat-number').forEach((el) => {
        const target = +el.dataset.target;
        const duration = 1400;
        const start = performance.now();
        const step = (now) => {
          const p = Math.min((now - start) / duration, 1);
          const ease = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(target * ease);
          if (p < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
      });
    });
  }, { threshold: 0.3 });
  counterObserver.observe(statsEl);
}

/* ── Smooth Scroll for Anchors ───────────────────────────────── */
document.querySelectorAll('a[href^="#"]').forEach((a) => {
  a.addEventListener('click', (e) => {
    const target = document.querySelector(a.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

/* ── Mobile Hamburger Menu ───────────────────────────────────── */
const hamburger = document.getElementById('nav-hamburger');
const navLinks = document.getElementById('nav-links');

if (hamburger && navLinks) {
  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    navLinks.classList.toggle('open');
  });

  navLinks.querySelectorAll('a').forEach((a) => {
    a.addEventListener('click', () => {
      hamburger.classList.remove('open');
      navLinks.classList.remove('open');
    });
  });

  document.addEventListener('click', (e) => {
    if (!hamburger.contains(e.target) && !navLinks.contains(e.target)) {
      hamburger.classList.remove('open');
      navLinks.classList.remove('open');
    }
  });
}
