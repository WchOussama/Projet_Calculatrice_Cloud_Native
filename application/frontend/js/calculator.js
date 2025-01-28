class Calculator {
    constructor() {
        this.display = document.querySelector('.main-display');
        this.memory = "";
        this.newNumber = true;
        this.bindEvents();
    }

    bindEvents() {
        document.querySelector('.calculator-keypad').addEventListener('click', (e) => {
            if (!e.target.matches('button')) return;
            const action = e.target.dataset.action;
            if (action) {
                this.handleOperator(action);
            } else {
                this.handleNumber(e.target.textContent);
            }
        });
    }

    handleNumber(num) {
        this.display.textContent = this.newNumber ? num : this.display.textContent + num;
        this.newNumber = false;
    }

    handleOperator(action) {
        if (action === "clear") {
            this.display.textContent = "0";
        } else if (action === "equals") {
            this.calculate();
        }
    }

    async calculate() {
        const response = await fetch('/api/calculate', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ expression: this.display.textContent })
        });
        const data = await response.json();
        this.display.textContent = data.result || "Error";
    }
}

document.addEventListener('DOMContentLoaded', () => new Calculator());
