document.addEventListener('DOMContentLoaded', function () {
	const toggle = document.querySelector('.nav-toggle');
	const nav = document.querySelector('.main-nav');

	if (toggle && nav) {
		toggle.addEventListener('click', function () {
			const isVisible = nav.style.display === 'flex' || nav.classList.contains('open');
			if (isVisible) {
				nav.style.display = 'none';
				nav.classList.remove('open');
			} else {
				nav.style.display = 'flex';
				nav.classList.add('open');
				nav.style.flexDirection = 'column';
				nav.style.position = 'absolute';
				nav.style.top = '90px';
				nav.style.right = '20px';
				nav.style.background = '#fff';
				nav.style.padding = '12px';
				nav.style.boxShadow = '0 6px 18px rgba(0,0,0,0.12)';
				nav.style.borderRadius = '10px';
			}
		});

		document.addEventListener('click', function (e) {
			if (!nav.contains(e.target) && !toggle.contains(e.target) && nav.classList.contains('open')) {
				nav.style.display = 'none';
				nav.classList.remove('open');
			}
		});
	}
});


