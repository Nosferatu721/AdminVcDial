let isPlaying = true;
const video = document.getElementById("video_bg");

if (video) {
  function reproducir() {
    video.play();
  }

  function pausar() {
    video.pause();
  }

  function keyboardmov(tm) {
    video.currentTime = tm;
  }

  $(document).ready(function () {
    pausar();
  });

  function move(tm) {
    const alActualizar = () => {
      if (video.currentTime >= tm - 0.05) {
        pausar();
      } else {
        window.requestAnimationFrame(alActualizar);
      }
    };
    window.requestAnimationFrame(alActualizar);
  }

  function detallar(posicion, cantidad) {
    video.currentTime = posicion;
    playVid();
    move(cantidad);
  }

  video.onplaying = function () {
    isPlaying = true;
  };

  video.onpause = function () {
    isPlaying = false;
  };

  function playVid() {
    if (video.paused && !isPlaying) {
      video.play();
    } else {
      setTimeout(() => {
        playVid();
      }, 2000);
    }
  }

  // TODO onclick="detallar(9, 13);"
  // let btn_login = document.getElementById("btn_login");
  // btn_login.addEventListener(
  //   "click",
  //   (e) => {
  //     e.preventDefault();
  //     setTimeout(() => {
  //       console.info("kjahsdjh");
  //       return true;
  //     }, 2000);
  //     console.info("kjahsdjh");
  //   },
  //   false
  // );
}
