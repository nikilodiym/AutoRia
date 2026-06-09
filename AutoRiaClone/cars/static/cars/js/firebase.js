import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.5/firebase-app.js";
import {
    getAuth,
    GoogleAuthProvider,
    signInWithPopup,
    signInWithRedirect,
    getRedirectResult
} from "https://www.gstatic.com/firebasejs/10.12.5/firebase-auth.js";

// 🔥 Firebase config
const firebaseConfig = {
    apiKey: "AIzaSyDerGahZ00OaopnqfQX8BQyDY-b6-rQ6t8",
    authDomain: "autoria-7c7af.firebaseapp.com",
    projectId: "autoria-7c7af",
    storageBucket: "autoria-7c7af.firebasestorage.app",
    messagingSenderId: "903578505474",
    appId: "1:903578505474:web:f98fbf714b132e458cb21b",
    measurementId: "G-D3R6039YND"
};

// init
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

const btn = document.getElementById("googleBtn");

/**
 * 🔁 Перевіряємо результат redirect (якщо popup не спрацює)
 */
getRedirectResult(auth)
    .then((result) => {
        if (result) {
            const user = result.user;
            console.log("REDIRECT USER:", user);

            user.getIdToken().then((token) => {
                console.log("TOKEN:", token);
            });
        }
    })
    .catch((error) => {
        console.error("Redirect error:", error);
    });

/**
 * 🔥 Логін
 */
btn.addEventListener("click", async () => {
    try {
        const result = await signInWithPopup(auth, provider);

        const user = result.user;
        const token = await user.getIdToken();

        console.log("USER:", user);
        console.log("TOKEN:", token);

        // TODO: Django API
        // await fetch("/api/firebase-login/", {
        //     method: "POST",
        //     headers: { "Content-Type": "application/json" },
        //     body: JSON.stringify({ token })
        // });

    } catch (error) {
        console.error("Google login error:", error.code);

        // 👇 якщо popup закрився — автоматично переходимо на redirect
        if (error.code === "auth/popup-closed-by-user") {
            console.log("Popup closed → switching to redirect...");
            signInWithRedirect(auth, provider);
            return;
        }

        alert(error.message);
    }
});