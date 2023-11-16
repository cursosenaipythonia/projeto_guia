function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  })
  .then(response => response.json())
  .then(data => {
    if (data.status === "success") {
      console.log("Nota excluída com sucesso!");
    } else if (data.status === "unauthorized") {
      console.error("Usuário não autorizado a excluir esta nota.");
    } else if (data.status === "not_found") {
      console.error("Nota não encontrada.");
    } else {
      console.error("Erro ao excluir nota.");
    }

    // Obtendo a parte da URL após o domínio (pathname)
    const currentPath = window.location.pathname;
    window.location.href = currentPath;  // Redireciona para a mesma página
  })
  .catch(error => {
    console.error("Erro durante a exclusão da nota:", error);
  });
}

/* Código de abertura e fechamento de menu mobile */

function menuShow() {

    let menuMobile = document.querySelector('.mobile-menu');

    if (menuMobile.classList.contains('open')) {

        menuMobile.classList.remove('open');

        document.querySelector('.icon').src = "static/menu.svg";

    } else {

        menuMobile.classList.add('open');

        document.querySelector('.icon').src = "static/close.svg";

    }

}