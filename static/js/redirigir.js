AFRAME.registerComponent('clickable', {
    schema: {default: ''},
    init: function () {
      this.el.addEventListener('click', () => {
        const url = this.data;
        window.location.href = url;
      });
    }
});
