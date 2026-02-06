const hero = document.getElementById("hero");

hero.addEventListener("click", (e) => {
    const rect = hero.getBoundingClientRect();

    for (let i = 0; i < 6; i++) {
        const bubble = document.createElement("span");
        bubble.className = "bubble";

        const size = Math.random() * 12 + 8;
        bubble.style.width = size + "px";
        bubble.style.height = size + "px";

        bubble.style.left = (e.clientX - rect.left + Math.random() * 30 - 15) + "px";
        bubble.style.top = (e.clientY - rect.top + Math.random() * 30 - 15) + "px";

        hero.appendChild(bubble);

        setTimeout(() => bubble.remove(), 3000);
    }
});

