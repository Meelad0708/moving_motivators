document.addEventListener('DOMContentLoaded', function() {
    const originalDropdown = document.querySelector('.motivator-dropdown');
    const container = document.querySelector('.dropdown-container');

    document.getElementById('moving_motivator').addEventListener('change', function() {
        const clone = originalDropdown.cloneNode(true);
        clone.querySelectorAll('option').forEach(option => {
            if (option.value === this.value) {
                option.remove();
            }
        });
        container.appendChild(clone);
    });
});
