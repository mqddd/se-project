const form = document.querySelector("#form")
form.addEventListener("submit", sendDataToBack)
function sendDataToBack() {
  const newPassword1 = document.getElementById("new_password1")
  const newPassword2 = document.getElementById("new_password2")
  const urlName = window.location.href
  const arraySplit = urlName.split("/")
  const uid64 = arraySplit[arraySplit.length - 1]
  const token = arraySplit[arraySplit.length - 2]
  axios.post("http://37.152.182.36:8000/api/rest-auth/password/reset/confirm/", {
      new_password1: newPassword1,
      new_password2: newPassword2,
      uid: uid64,
      token: token,
    })
    .then(() => console.log("ok"))
    .catch((err) => console.log(error))
}
