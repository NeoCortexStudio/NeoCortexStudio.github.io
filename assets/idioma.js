/* Español / inglés: ?lang=en o ?lang=es en la dirección manda; si no, lo que eligió antes o el idioma del navegador. */
(function () {
  var q = /[?&]lang=(es|en)/.exec(location.search), guardado = null;
  try { guardado = localStorage.getItem('nc-idioma'); } catch (e) {}
  var nav = (navigator.language || 'es').toLowerCase().indexOf('es') === 0 ? 'es' : 'en';
  var id = (q && q[1]) || guardado || nav;
  function pon(x) {
    id = x; document.documentElement.setAttribute('data-idioma', x); document.documentElement.lang = x;
    var t = document.querySelector('title[data-es]'); if (t) document.title = t.getAttribute('data-' + x);
    var bs = document.querySelectorAll('.idioma button');
    for (var i = 0; i < bs.length; i++) bs[i].classList.toggle('on', bs[i].getAttribute('data-l') === x);
  }
  pon(id);
  document.addEventListener('DOMContentLoaded', function () {
    pon(id);
    var bs = document.querySelectorAll('.idioma button');
    for (var i = 0; i < bs.length; i++) bs[i].addEventListener('click', function () {
      var x = this.getAttribute('data-l'); try { localStorage.setItem('nc-idioma', x); } catch (e) {} pon(x);
    });
  });
})();
