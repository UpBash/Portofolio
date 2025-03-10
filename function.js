// Open and Close PDF Viewer
function openPDF(pdfFile) {
    document.getElementById("pdfViewer").style.display = "block";
    document.getElementById("pdfFrame").src = pdfFile;
}

function closePDF() {
    document.getElementById("pdfViewer").style.display = "none";
    document.getElementById("pdfFrame").src = "";
}

// Toggle Document Options
function toggleOptions(element) {
    let options = element.querySelector(".doc-options");
    options.style.display = options.style.display === "flex" ? "none" : "flex";
}
let previousEquations = [];

function drawEquation(equation) {
    let body = document.body;
    let bodyWidth = window.innerWidth;
    let bodyHeight = window.innerHeight;

    let x, y;
    let validPosition = false;
    let maxAttempts = 10;

    // Try placing equation in a random position on the screen
    while (!validPosition && maxAttempts > 0) {
        x = Math.random() * bodyWidth; // Random horizontal position across the screen
        y = Math.random() * bodyHeight; // Random vertical position across the screen

        // Check if the new equation overlaps with previous ones
        validPosition = previousEquations.every(pos => {
            let dx = Math.abs(pos.x - x);
            let dy = Math.abs(pos.y - y);
            return dx > 100 && dy > 100; // Ensure spacing between equations
        });

        maxAttempts--;
    }

    // Store the new equation position
    previousEquations.push({ x, y });

    let equationElement = document.createElement("div");
    equationElement.classList.add("math-equation");
    equationElement.style.position = "fixed";  // Position fixed to screen
    equationElement.style.left = `${x}px`;
    equationElement.style.top = `${y}px`;
    equationElement.style.opacity = "1";
    equationElement.textContent = equation;

    // Style the equation
    equationElement.style.fontSize = "30px";  // Set font size
    equationElement.style.fontFamily = "'Courier New', monospace";  // Set font family
    equationElement.style.color = "black";  // Set text color to black
    equationElement.style.textAlign = "center";
    equationElement.style.zIndex = "-1";  // Place it behind all other content
    equationElement.style.pointerEvents = "none";  // Disable interaction

    // Append the equation to the body
    body.appendChild(equationElement);

    // Fade out and remove the equation after 12 seconds
    setTimeout(() => {
        equationElement.style.transition = "opacity 2s";
        equationElement.style.opacity = "0";
        setTimeout(() => {
            equationElement.remove();
        }, 2000);
    }, 12000); // Equation visible for 12 seconds before fading out
}

// Generate random math equations every 5 seconds
setInterval(drawRandomMath, 5000);

// Random math equations to draw
function drawRandomMath() {
    let equations = [
        "∫ f(x) dx", "E = mc²", "π ≈ 3.1415926535",
        "a² + b² = c²", "∂/∂x", "lim x→∞",
        "∂u/∂t = Δu + u - u³", "y = Wx + b",
        "model.fit(X, y)", "loss.backward()",
        "∇ × E = -∂B/∂t", "∇ ⋅ B = 0",
        "HΨ = EΨ", "F = ma", "σ = F/A",
        "P(A | B) = P(B | A) * P(A) / P(B)",
        "∑_{i=1}^{n} x_i", "∇²φ = 0", "e^{iπ} + 1 = 0",
        "i² = -1", "f''(x) = 6x - 4", "cos²θ + sin²θ = 1",
        "∂L/∂θ = 0", "y = mx + c", "∫ e^x dx = e^x + C",
        "Softmax(x) = e^x / ∑ e^x", "σ(x) = 1 / (1 + e^{-x})",
        "H(X) = -∑ p(x) log p(x)", "∫ e^{-x²} dx = √π",
        "W_{t+1} = W_t - α∇J(W_t)", "∂J/∂W = X^T(XW - Y)",
        "L = ∑ log p(y_i | x_i)", "X_{t+1} = AX_t + BU_t",
        "det(A) = Π λ_i", "P(E) = |E| / |Ω|", "ψ(t) = e^{-at} cos(bt)",
        "z = x + iy", "LSTM: f_t = σ(W_f [h_{t-1}, x_t] + b_f)"
    ];

    let equation = equations[Math.floor(Math.random() * equations.length)];
    drawEquation(equation);
}

// Generate math equations inside the hero-container every 5 seconds
setInterval(drawRandomMath, 5000);

// Smooth Scroll for Button Clicks (if links lead to sections)
document.querySelectorAll(".button").forEach(button => {
    button.addEventListener("click", function(e) {
        e.preventDefault();
        let target = document.querySelector(this.getAttribute("href"));
        if (target) {
            target.scrollIntoView({ behavior: "smooth" });
        }
    });
});

// ✅ Close collapsible section when clicking outside of it
document.addEventListener("click", function (event) {
    let openSection = document.querySelector(".collapsible-section.active");
    
    if (openSection && !openSection.contains(event.target) && !event.target.closest(".project")) {
        toggleSection(openSection.id);
    }
});

// When the project section opens, disable scrolling, hover, and clicks on the main page
function toggleSection(sectionId) {
    let section = document.getElementById(sectionId);
    let body = document.body;

    // If section is already open, close it
    if (section.classList.contains('active')) {
        section.classList.remove('active');
        setTimeout(() => {
            section.style.display = "none";
            body.classList.remove("no-scroll");  // Re-enable scrolling and clicks
            body.classList.add("scroll-enabled"); // Allow interactions
        }, 500); // Match transition time
        return;
    }

    // Close all sections before opening the selected one
    document.querySelectorAll('.collapsible-section').forEach(sec => {
        if (sec !== section) { // Don't close the section we're opening
            sec.classList.remove('active');
            setTimeout(() => {
                sec.style.display = "none";
            }, 500);
        }
    });

    // Show the selected section and disable scrolling, hover, and clicks
    setTimeout(() => {
        section.style.display = "block";
        setTimeout(() => {
            section.classList.add('active');
            body.classList.add("no-scroll");  // Lock main page
            body.classList.remove("scroll-enabled"); // Disable hover/clicks
        }, 10); // Small delay ensures it doesn't collapse instantly
    }, 100);
}




// ✅ Handle project clicks to open the project window and show correct details
document.querySelectorAll('.project').forEach(project => {
    project.addEventListener('click', function () {
        // Remove active class from all projects
        document.querySelectorAll('.project').forEach(proj => proj.classList.remove('active'));

        // Mark the clicked project
        this.classList.add('active');

        // ✅ Get project name from the h3 text inside the rectangle
        let projectTitle = this.querySelector("h3").innerText.trim();  

        // ✅ Convert project title to match projectData keys
        let projectKey = Object.keys(projectData).find(key => 
            projectData[key].title.toLowerCase() === projectTitle.toLowerCase()
        );

        if (!projectKey) return; 

        // ✅ Open the projects section
        toggleSection('projects');

        // ✅ Show correct project details (with delay to ensure visibility)
        setTimeout(() => {
            showProjectDetails(projectKey);
        }, 200);
    });
});




// Project descriptions
const projectData = {
    "thesis": {
        title: "Thesis",
        description: "An in-depth exploration of deterministic and stochastic partial differential equations...",
        file: "https://upbash.github.io/Portofolio/thesis.pdf"
    },
    "data-mining": {
        title: "Data Mining and Preprocessing",
        description: "A research study on preprocessing techniques in AI pipelines...",
        file: "data-mining.pdf"
    },
    "ml-models-wild": {
        title: "Machine Learning Models (Forest Wildfires)",
        description: "Exploring various machine learning models and their applications...",
        file: "ml-models(w).pdf"
    },
    "ml-models-auc": {
        title: "Machine Learning Models (Auction Sales)",
        description: "Exploring various ma...",
        file: "ml-models(a).pdf"
    },
    "computer-vision": {
        title: "Computer Vision",
        description: "A study on the implementation of modern computer vision techniques...",
        file: "computer-vision.pdf"
    },
    "predictive-analytics": {
        title: "Predictive Analytics",
        description: "Research on time series forecasting and statistical prediction models...",
        file: "predictive-analytics.pdf"
    },
    "business-analytics": {
        title: "Business Process Analytics",
        description: "Analyzing business processes using AI and automation...",
        file: "business-analytics.pdf"
    },
    "pca-lda": {
        title: "PCA & LDA",
        description: "Dimensionality reduction techniques applied in machine learning...",
        file: "pca-lda.pdf"
    },
    "nlp": {
        title: "NLP",
        description: "nlpnlpnlpnlp",
        file: "nlp.pdf"
    }
    
};

function showProjectDetails(projectKey) {
    let project = projectData[projectKey];

    if (project) {
        document.getElementById("project-title").innerText = project.title;
        document.getElementById("project-description").innerText = project.description;

        let downloadButton = document.getElementById("download-button");

        // ✅ Update the download button and make it visible
        downloadButton.href = project.file;  // Dynamically set the correct file path
        downloadButton.classList.remove("hidden");  // Make the button visible

        // Ensure the filename is valid for the download attribute (strip path if necessary)
        const fileName = project.file.split('/').pop();  // Get the file name without path

        if (fileName) {
            downloadButton.download = fileName;  // Set the download attribute to the file name
        }
    }
}
// Handle project clicks to open the project window and show correct details
document.querySelectorAll('.project').forEach(project => {
    project.addEventListener('click', function () {
        // Get the project name from the clicked item
        let projectTitle = this.querySelector("h3").innerText.trim();

        // Match the project title to the projectData keys
        let projectKey = Object.keys(projectData).find(key => 
            projectData[key].title.toLowerCase() === projectTitle.toLowerCase()
        );

        if (!projectKey) return;  // Exit if no match is found

        // Update the project details
        showProjectDetails(projectKey);

        // Optionally open the projects section if it's not already open
        toggleSection('projects');
    });
});
