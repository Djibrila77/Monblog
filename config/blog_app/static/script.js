

window.onbeforeunload = function () {
    window.scrollTo(0, 0);
};

function toggleText(btn) {
    // On trouve l'extrait et le texte complet dans la même carte
    const parent = btn.parentElement;
    const extrait = parent.querySelector('.extrait');
    const complet = parent.querySelector('.complet');

            if (complet.style.display === "none") {
                complet.style.display = "inline"; // Affiche tout
                extrait.style.display = "none";   // Cache l'extrait
                btn.innerHTML = "Voir moins";     // Change le texte du bouton
            } else {
                complet.style.display = "none";   // Cache le texte complet
                extrait.style.display = "inline"; // Réaffiche l'extrait
                btn.innerHTML = "Voir plus";      // Remet le bouton d'origine
            }
        }
                
        
    