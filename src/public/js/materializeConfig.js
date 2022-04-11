document.addEventListener("DOMContentLoaded", function () {
  window.elemsModal = document.querySelectorAll(".modal");
  M.Modal.init(elemsModal);
  let elemsSelect = document.querySelectorAll("#selectCamp");
  M.FormSelect.init(elemsSelect);
  $("input[data-length]").characterCounter();
});
