const getData = async (route) => {
  try {
    let res = await fetch(route);
    let json = await res.json();
    if (!res.ok) throw { status: res.status, statusTect: res.statusText };
    return json;
  } catch (err) {
    console.log(err);
  }
};

const postData = async (route, data = {}) => {
  try {
    let res = await fetch(route, {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    });
    let json = await res.json();

    if (!res.ok) throw { status: res.status, statusTect: res.statusText };
    return json;
  } catch (err) {
    console.log(err);
  }
};

const deleteData = async (route) => {
  try {
    let res = await fetch(route, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    });
    let json = await res.json();
    if (!res.ok) throw { status: res.status, statusTect: res.statusText };
    return json;
  } catch (err) {
    console.log(err);
  }
};

const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 4000,
  timerProgressBar: true,
  didOpen: (toast) => {
    toast.addEventListener("mouseenter", Swal.stopTimer);
    toast.addEventListener("mouseleave", Swal.resumeTimer);
  },
});

const inputsMayus = (arrInputs = []) => {
  arrInputs.forEach((element) => {
    element.addEventListener("keyup", (e) => {
      element.value = element.value.toUpperCase();
    });
  });
};

const limpiarCampos = (arrInputs = []) => {
  arrInputs.forEach((element) => {
    element.value = "";
    element.nextElementSibling.classList.remove("active");
  });
};

const mensajeBienvenido = () => {
  const divBienvenido = document.getElementById("bienvenido");
  if (!divBienvenido) return;
  let user = divBienvenido.dataset.user;
  Toast.fire({
    icon: "success",
    title: `Bienvenido ${user}`,
  });
};

document.addEventListener("DOMContentLoaded", (e) => {
  setTimeout(() => {
    mensajeBienvenido();
  }, 10);
});
