(function(){
  document.documentElement.classList.remove('no-js');
  var nav=document.querySelector('.nav'),burger=document.querySelector('.burger'),scrim=document.querySelector('.scrim'),closeB=document.querySelector('.nav-close');
  function setNav(o){nav.classList.toggle('open',o);scrim.classList.toggle('show',o);burger.setAttribute('aria-expanded',o);document.body.style.overflow=o?'hidden':'';}
  if(burger){burger.addEventListener('click',function(){setNav(!nav.classList.contains('open'))});scrim.addEventListener('click',function(){setNav(false)});closeB&&closeB.addEventListener('click',function(){setNav(false)});}
  document.querySelectorAll('.dd>button').forEach(function(b){b.addEventListener('click',function(){var d=b.parentNode;var o=!d.classList.contains('open');d.classList.toggle('open',o);b.setAttribute('aria-expanded',o)})});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'){setNav(false);document.querySelectorAll('.dd.open').forEach(function(d){d.classList.remove('open')})}});

  // Photo bands: true "see-through" fixed background on desktop; smooth transform parallax on touch/iOS (no background-attachment:fixed there)
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine=window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var iOS=/iP(ad|hone|od)/.test(navigator.platform)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
  var bands=[].slice.call(document.querySelectorAll('.band'));
  if(!reduce&&fine&&!iOS){bands.forEach(function(b){b.classList.add('fixed')});}
  else if(!reduce&&bands.length){
    var ticking=false;
    function update(){var vh=window.innerHeight;bands.forEach(function(b){var r=b.getBoundingClientRect();if(r.bottom<-50||r.top>vh+50)return;var p=(r.top+r.height/2-vh/2)/(vh/2+r.height/2);p=Math.max(-1,Math.min(1,p));var bg=b.querySelector('.band__bg');bg.style.transform='translate3d(0,'+(-p*r.height*0.16).toFixed(1)+'px,0)';});ticking=false;}
    window.addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(update)}},{passive:true});
    window.addEventListener('resize',update);update();
  }
  // gentle reveal
  if('IntersectionObserver' in window&&!reduce){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px'});document.querySelectorAll('.reveal').forEach(function(el){io.observe(el)});}
  else document.querySelectorAll('.reveal').forEach(function(el){el.classList.add('in')});
})();
(function(){if(window.innerWidth<=820){document.querySelectorAll('[data-sm]').forEach(function(el){el.style.backgroundImage="url('"+el.getAttribute('data-sm')+"')"})}})();
