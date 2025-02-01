fetch('/api/login', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        email: 'thedylanwhitney@gmail.com',
        password: 'password123',
    }),
});
