const projectData = {
    thesis: {
        title: "Thesis",
        description: "Master's thesis on deterministic and stochastic partial differential equations with machine learning approaches.",
        file: "assets/docs/projects/thesis.pdf"
    },
    nlp: {
        title: "NLP",
        description: "Comparative NLP project evaluating multiple language processing strategies and model behaviors.",
        file: "assets/docs/projects/nlp.pdf"
    },
    "data-mining": {
        title: "Data Mining",
        description: "Data mining and preprocessing pipeline work focused on feature quality and robust analysis inputs.",
        file: "assets/docs/projects/data-mining.pdf"
    },
    "ml-models-wild": {
        title: "ML: Forest Wildfires",
        description: "Machine learning models for wildfire prediction and risk estimation with feature-driven evaluation.",
        file: "assets/docs/projects/ml-models(w).pdf"
    },
    "ml-models-auc": {
        title: "ML: Auction Sales",
        description: "Supervised learning models for auction sales forecasting with model comparison and validation metrics.",
        file: "assets/docs/projects/ml-models(a).pdf"
    },
    "computer-vision": {
        title: "Computer Vision",
        description: "Computer vision workflows and model experiments for recognition and visual pattern extraction tasks.",
        file: "assets/docs/projects/computer-vision.pdf"
    },
    "predictive-analytics": {
        title: "Predictive Analytics",
        description: "Forecasting-oriented analytics using time-series and supervised methods for predictive decision support.",
        file: "assets/docs/projects/predictive-analytics.pdf"
    },
    "business-analytics": {
        title: "Business Analytics",
        description: "Business process analytics with data-driven insights and practical optimization recommendations.",
        file: "assets/docs/projects/business-analytics.pdf"
    },
    "pca-lda": {
        title: "PCA & LDA",
        description: "Dimensionality reduction study using PCA and LDA for signal clarity and classification performance.",
        file: "assets/docs/projects/pca-lda.pdf"
    }
};

const cards = Array.from(document.querySelectorAll(".project-card"));
const titleNode = document.getElementById("project-title");
const descriptionNode = document.getElementById("project-description");
const downloadButton = document.getElementById("download-button");

function setActiveProject(projectKey) {
    const project = projectData[projectKey];
    if (!project || !titleNode || !descriptionNode || !downloadButton) {
        return;
    }

    cards.forEach(card => {
        card.classList.toggle("active", card.dataset.project === projectKey);
    });

    titleNode.textContent = project.title;
    descriptionNode.textContent = project.description;
    downloadButton.href = project.file;
    downloadButton.download = project.file.split("/").pop();
}

cards.forEach(card => {
    card.addEventListener("click", () => {
        setActiveProject(card.dataset.project);
    });
});

if (cards.length > 0) {
    const initial = cards.find(card => card.classList.contains("active")) || cards[0];
    setActiveProject(initial.dataset.project);
}


