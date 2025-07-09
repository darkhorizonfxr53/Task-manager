document.addEventListener('DOMContentLoaded', () => {
    const deleteLinks = document.querySelectorAll('a[href^="/delete/"]');

    deleteLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            const confirmed = confirm("Are you sure you want to delete this task?");
            if (!confirmed) {
                event.preventDefault();
            }
        });
    });
});
