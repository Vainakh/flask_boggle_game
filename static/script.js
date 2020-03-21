async function getWordFromForm() {
  let word = $('#word-submission').value;
  response = await axios.post('http://localhost:5000/check-word', {word});
  return response.data;
}

$('form').on('submit', (event) => {
  event.preventDefault()
  response = getWordFromForm()
})