const body = document.body;
const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("messageInput");
const typingIndicator = document.getElementById("typing");
const messages = document.getElementById("messages");
const userMessage = document.querySelector("[data-user-message]");
const botResponse = document.querySelector("[data-bot-response]");
const welcomeBubble = document.getElementById("welcomeBubble");
const closeWelcome = document.getElementById("closeWelcome");

const welcomeStorageKey = "ngi-bot-welcome-dismissed";

const moodRules = [
    {
        className: "mood-sadness",
        keywords: ["tristeza", "triste", "desanimado", "cansado"],
    },
    {
        className: "mood-anxiety",
        keywords: ["ansiedad", "preocupado", "preocupacion"],
    },
    {
        className: "mood-fear",
        keywords: ["miedo", "temor", "inseguro"],
    },
    {
        className: "mood-gratitude",
        keywords: ["agradecido", "gracias", "feliz", "alegria"],
    },
    {
        className: "mood-hope",
        keywords: ["esperanza", "fe", "confianza"],
    },
    {
        className: "mood-love",
        keywords: ["amor", "paz"],
    },
];

const moodClasses = moodRules.map((rule) => rule.className);

function normalizeText(value) {
    return value
        .toLocaleLowerCase("es")
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "");
}

function cleanText(value) {
    return value
        .replace(/\s+/g, " ")
        .replace(/\s+([.,;:!?])/g, "$1")
        .trim();
}

function applyEmotionalAtmosphere(value) {
    const words = new Set(normalizeText(value).split(/[^a-zñ]+/).filter(Boolean));
    const matchingRule = moodRules.find((rule) =>
        rule.keywords.some((keyword) => words.has(keyword))
    );

    body.classList.remove(...moodClasses);

    if (matchingRule) {
        body.classList.add(matchingRule.className);
    }

    body.dataset.mood = matchingRule
        ? matchingRule.className.replace("mood-", "")
        : "neutral";
}

function createResponseSection(icon, label, text, extraClass = "") {
    const section = document.createElement("section");
    section.className = "response-section";

    const heading = document.createElement("p");
    heading.className = "response-label";
    heading.textContent = `${icon} ${label}`;

    const content = document.createElement("p");
    content.className = `response-text ${extraClass}`.trim();
    content.textContent = cleanText(text);

    section.append(heading, content);
    return section;
}

function createVerseSection(reference, verse) {
    const section = document.createElement("section");
    section.className = "response-section";

    const heading = document.createElement("p");
    heading.className = "response-label";
    heading.textContent = "📖 VERSÍCULO";

    const content = document.createElement("p");
    content.className = "response-text verse-text";

    const fullVerse = cleanText(`${reference} ${verse}`);
    content.textContent = fullVerse;

    section.append(heading, content);
    return section;
}

function formatBotResponse() {
    if (!botResponse) {
        return;
    }

    const responseText = botResponse.innerText.trim();

    const structuredMatch = responseText.match(
        /REFERENCIA\s*:\s*([\s\S]*?)\s*VERS(?:Í|I)CULO\s*:\s*([\s\S]*?)\s*REFLEXI(?:Ó|O)N\s*:\s*([\s\S]*?)(?:\s*APLICACI(?:Ó|O)N\s*PR(?:Á|A)CTICA\s*:\s*([\s\S]*))?$/i
    );

    if (structuredMatch) {
        const reference = cleanText(structuredMatch[1] || "");
        const verse = cleanText(structuredMatch[2] || "");
        const reflection = cleanText(structuredMatch[3] || "");
        const application = cleanText(structuredMatch[4] || "");

        const sections = [];

        if (reference || verse) {
            sections.push(createVerseSection(reference, verse));
        }

        if (reflection) {
            sections.push(createResponseSection("💡", "REFLEXIÓN", reflection));
        }

        if (application) {
            sections.push(createResponseSection("🤲", "APLICACIÓN PRÁCTICA", application));
        }

        if (sections.length > 0) {
            botResponse.replaceChildren(...sections);
        }

        return;
    }

    const markerMatch = responseText.match(/Interpretaci(?:ó|o)n\s*:/i);

    if (!markerMatch || markerMatch.index === undefined) {
        botResponse.textContent = cleanText(responseText);
        return;
    }

    const citation = cleanText(
        responseText
            .slice(0, markerMatch.index)
            .replace(/^📖\s*/, "")
    );

    const reflection = cleanText(
        responseText.slice(markerMatch.index + markerMatch[0].length)
    );

    if (!citation || !reflection) {
        botResponse.textContent = cleanText(responseText);
        return;
    }

    botResponse.replaceChildren(
        createVerseSection(citation, ""),
        createResponseSection("💡", "REFLEXIÓN", reflection)
    );
}

function wasWelcomeDismissed() {
    try {
        return sessionStorage.getItem(welcomeStorageKey) === "true";
    } catch {
        return false;
    }
}

function rememberWelcomeDismissal() {
    try {
        sessionStorage.setItem(welcomeStorageKey, "true");
    } catch {
        // The bubble remains closable even when browser storage is unavailable.
    }
}

function dismissWelcome() {
    if (!welcomeBubble || welcomeBubble.hidden) {
        return;
    }

    welcomeBubble.classList.add("is-closing");
    rememberWelcomeDismissal();

    window.setTimeout(() => {
        welcomeBubble.hidden = true;
        welcomeBubble.classList.remove("is-closing");
    }, 260);
}

formatBotResponse();
applyEmotionalAtmosphere(userMessage ? userMessage.textContent : "");

if (welcomeBubble && wasWelcomeDismissed()) {
    welcomeBubble.hidden = true;
}

if (closeWelcome) {
    closeWelcome.addEventListener("click", dismissWelcome);
}

if (messageInput) {
    messageInput.addEventListener("input", () => {
        applyEmotionalAtmosphere(messageInput.value);
    });
}

if (messages) {
    messages.scrollTop = messages.scrollHeight;
}

if (chatForm && typingIndicator) {
    chatForm.addEventListener("submit", () => {
        applyEmotionalAtmosphere(messageInput ? messageInput.value : "");
        typingIndicator.hidden = false;
    });
}