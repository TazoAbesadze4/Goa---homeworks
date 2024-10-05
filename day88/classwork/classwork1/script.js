const form = document.getElementById('myForm');
const tableBody = document.getElementById('tableBody');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password'.value);

    if(name && email && password) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${name}</td>
            <td>${email}</td>
            <td>${password}</td>
        `;

        tableBody.appendChild(row);

        document.getElementById('name').value = '';
        document.getElementById('email').value = '';
        document.getElementById('password').value = '';
    } else {
        alert('please fill in both fields. ');
    }
})
// es kodi ar mushaobs