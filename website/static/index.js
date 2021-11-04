/* 
This function is basically taking about noteId that we passed
and it is going to send a POST request to the /delete-note endpoint
when it gets a response then it is going to reload the window
*/
function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }