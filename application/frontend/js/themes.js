const themes = {
    naruto: {
        name: "Naruto",
        colors: {
            primary: "#FF9800",
            secondary: "#FFC107",
            accent: "#2196F3",
            text: "#000000"
        },
        icon: "🍥",
        background: "linear-gradient(135deg, #FF9800, #FFC107)"
    },
    demonSlayer: {
        name: "Demon Slayer",
        colors: {
            primary: "#4CAF50",
            secondary: "#000000",
            accent: "#FF5252",
            text: "#FFFFFF"
        },
        icon: "⚔️",
        background: "linear-gradient(135deg, #4CAF50, #000000)"
    },
    onePiece: {
        name: "One Piece",
        colors: {
            primary: "#F44336",
            secondary: "#FFD700",
            accent: "#FFD700",
            text: "#FFFFFF"
        },
        icon: "🏴‍☠️",
        background: "linear-gradient(135deg, #F44336, #FFD700)"
    },
    attackOnTitan: {
        name: "Attack on Titan",
        colors: {
            primary: "#424242",
            secondary: "#616161",
            accent: "#B71C1C",
            text: "#FFFFFF"
        },
        icon: "⚔️",
        background: "linear-gradient(135deg, #424242, #212121)"
    },
    dragonBall: {
        name: "Dragon Ball",
        colors: {
            primary: "#FF5722",
            secondary: "#FFC107",
            accent: "#2196F3",
            text: "#FFFFFF"
        },
        icon: "🔮",
        background: "linear-gradient(135deg, #FF5722, #FFC107)"
    }
};

class ThemeManager {
    constructor() {
        this.currentTheme = 'naruto';
        this.themeButton = document.querySelector('.theme-button');
        this.themeName = document.querySelector('.theme-name');
        
        this.init();
    }

    init() {
        this.applyTheme(this.currentTheme);
        this.themeButton.addEventListener('click', () => this.cycleTheme());
    }

    applyTheme(themeName) {
        const theme = themes[themeName];
        document.documentElement.style.setProperty('--primary-color', theme.colors.primary);
        document.documentElement.style.setProperty('--secondary-color', theme.colors.secondary);
        document.documentElement.style.setProperty('--accent-color', theme.colors.accent);
        document.documentElement.style.setProperty('--text-color', theme.colors.text);
        document.body.style.background = theme.background;
        this.themeName.textContent = `${theme.name} ${theme.icon}`;
    }

    cycleTheme() {
        const themeNames = Object.keys(themes);
        const currentIndex = themeNames.indexOf(this.currentTheme);
        const nextIndex = (currentIndex + 1) % themeNames.length;
        this.currentTheme = themeNames[nextIndex];
        this.applyTheme(this.currentTheme);
    }
}
