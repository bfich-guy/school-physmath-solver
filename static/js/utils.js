import { calculateEndpoint, FormulasData } from "./config.js";


// Helpers

export function areObjectsNull({
    objects,
}) {
    let areObjectsNull = false;

    for (const object of objects) {
        const objectIsNull = object === null || object === undefined;

        if (objectIsNull) {
            return true;
        }
    }

    return areObjectsNull;
};


export function parseUserFormulaName({
    userFormulaName,
}) {
    const parsedUserFormulaName = userFormulaName.trim().toLowerCase();
    return parsedUserFormulaName;
};


// Server

export function calculateFormula() {
    for (const [buttonId, buttonData] of Object.entries(FormulasData)) {
        const formulaButtonWidget = document.getElementById(buttonId);
        const formulaButtonDoesNotExist = areObjectsNull({objects: [formulaButtonWidget]});

        if (formulaButtonDoesNotExist) {
            continue;
        };

        formulaButtonWidget.addEventListener("click", () => {
            const request = {};
            const quantitiesInputData = buttonData["input"];
            const quantitiesOutputData = buttonData["output"];
            const formula = buttonData["formula"];

            const buttonDataIsNull = areObjectsNull({objects: [quantitiesInputData, quantitiesOutputData, formula]});

            if (buttonDataIsNull) {
                console.log(buttonId);
                return null;
            };

            request["formula"] = formula;
            request["quantities"] = {};

            for (const [inputId, inputData] of Object.entries(quantitiesInputData)) {
                const quantityInputWidget = document.getElementById(inputId);
                const quantityInputValue = quantityInputWidget.value;
                const quantityInputName = inputData["name"];
                const quantityInputMode = inputData["mode"];

                const quantityDataIsNull = areObjectsNull({objects: [quantityInputWidget, quantityInputValue, quantityInputName, quantityInputMode]});

                if (quantityDataIsNull) {
                    return null;
                };

                request["quantities"][quantityInputName] = {
                    "value": quantityInputValue,
                    "mode": quantityInputMode,
                };
            }

            fetch(calculateEndpoint, {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(request)
            })
            .then(response => {
                const responseDoesNotExist = !response.ok;

                if (responseDoesNotExist) {
                    return null;
                } else {
                    return response.json();
                };
            })
            .then(data => {
                const formulaAnswer = data.answer;
                const formulaAnswerId = quantitiesOutputData["id"];

                const formulaDataIsNull = areObjectsNull({objects: [formulaAnswer, formulaAnswerId]});

                if (formulaDataIsNull) {
                    return null;
                };

                const formulaAnswerWidget = document.getElementById(formulaAnswerId);
                formulaAnswerWidget.textContent = formulaAnswer;
            })
        });
    };
};


export function searchFormula() {
    const formulasGridWidget = document.getElementById("formulas-grid");
    const formulaSearchingInputWidget = document.getElementById("formula-searching-input");

    formulaSearchingInputWidget.addEventListener('input', () => {
        for (const formulaCardWidget of formulasGridWidget.children) {
            const formulaNameWidget = formulaCardWidget.getElementsByClassName("formula-name")[0];
            const formulaNameValue = parseUserFormulaName({userFormulaName: formulaNameWidget.textContent});
            const formulaSearchingInputValue = parseUserFormulaName({userFormulaName: formulaSearchingInputWidget.value});
            const formulaIsFound = formulaNameValue.includes(formulaSearchingInputValue);

            if (formulaIsFound) {
                formulaCardWidget.style.display = '';
            } else {
                formulaCardWidget.style.display = 'none';
            };
        };
    });
};
