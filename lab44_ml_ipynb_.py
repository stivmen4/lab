{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vn24-SCbEOe2"
      },
      "source": [
        "# Машинне навчання\n",
        "\n",
        "## Опис\n",
        "\n",
        "В цій лабораторній ви будете працювати з набором даних [UCI Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality). Він містить 11 фіч.\n",
        "\n",
        "## Підготовка"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ey9tzvWyEOe_"
      },
      "outputs": [],
      "source": [
        "%%capture\n",
        "%pip install pandas seaborn scikit-learn"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "caOUi0RHEOfC"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import seaborn as sns\n",
        "\n",
        "%matplotlib inline"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "D7NkuIFuEOfD"
      },
      "source": [
        "## Читання даних\n",
        "В процессі читання даних ми додаємо 12-ту фічу - колір вина."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "4fW52IXdEOfD"
      },
      "outputs": [],
      "source": [
        "# Завантажуємо червоне вино\n",
        "dfr = pd.read_csv(\"https://raw.githubusercontent.com/stivmen4/lab/blob/main/winequality-red.csv", sep=',')\n",
        "dfr['color'] = 'red'\n",
        "# Завантажуємо біле вино\n",
        "dfw = pd.read_csv(\"https://raw.githubusercontent.com/stivmen4/lab/blob/main/winequality-white.csv", sep=',')\n",
        "dfw['color'] = 'white'\n",
        "# Об’єднання та перемішування даних\n",
        "df = pd.concat([dfr, dfw])\n",
        "df = df.sample(frac=1, random_state=3).reset_index(drop=True)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "AsyxnO0yEOfE"
      },
      "source": [
        "## Огляд даних"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "h_R1FavsEOfF",
        "outputId": "f0667ec4-ab25-41c8-faa8-c2224382f88c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        }
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   fixed acidity  volatile acidity  citric acid  residual sugar  chlorides  \\\n",
              "0            5.9             0.180         0.28             1.0      0.037   \n",
              "1           10.2             0.670         0.39             1.9      0.054   \n",
              "2            8.4             0.715         0.20             2.4      0.076   \n",
              "3            6.8             0.370         0.51            11.8      0.044   \n",
              "4            8.9             0.750         0.14             2.5      0.086   \n",
              "\n",
              "   free sulfur dioxide  total sulfur dioxide  density    pH  sulphates  \\\n",
              "0                 24.0                  88.0  0.99094  3.29       0.55   \n",
              "1                  6.0                  17.0  0.99760  3.17       0.47   \n",
              "2                 10.0                  38.0  0.99735  3.31       0.64   \n",
              "3                 62.0                 163.0  0.99760  3.19       0.44   \n",
              "4                  9.0                  30.0  0.99824  3.34       0.64   \n",
              "\n",
              "   alcohol  quality  color  \n",
              "0    10.65        7  white  \n",
              "1    10.00        5    red  \n",
              "2     9.40        5    red  \n",
              "3     8.80        5  white  \n",
              "4    10.50        5    red  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-46efddd7-4f95-4a18-8228-8526af474fe2\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>fixed acidity</th>\n",
              "      <th>volatile acidity</th>\n",
              "      <th>citric acid</th>\n",
              "      <th>residual sugar</th>\n",
              "      <th>chlorides</th>\n",
              "      <th>free sulfur dioxide</th>\n",
              "      <th>total sulfur dioxide</th>\n",
              "      <th>density</th>\n",
              "      <th>pH</th>\n",
              "      <th>sulphates</th>\n",
              "      <th>alcohol</th>\n",
              "      <th>quality</th>\n",
              "      <th>color</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>5.9</td>\n",
              "      <td>0.180</td>\n",
              "      <td>0.28</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.037</td>\n",
              "      <td>24.0</td>\n",
              "      <td>88.0</td>\n",
              "      <td>0.99094</td>\n",
              "      <td>3.29</td>\n",
              "      <td>0.55</td>\n",
              "      <td>10.65</td>\n",
              "      <td>7</td>\n",
              "      <td>white</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>10.2</td>\n",
              "      <td>0.670</td>\n",
              "      <td>0.39</td>\n",
              "      <td>1.9</td>\n",
              "      <td>0.054</td>\n",
              "      <td>6.0</td>\n",
              "      <td>17.0</td>\n",
              "      <td>0.99760</td>\n",
              "      <td>3.17</td>\n",
              "      <td>0.47</td>\n",
              "      <td>10.00</td>\n",
              "      <td>5</td>\n",
              "      <td>red</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>8.4</td>\n",
              "      <td>0.715</td>\n",
              "      <td>0.20</td>\n",
              "      <td>2.4</td>\n",
              "      <td>0.076</td>\n",
              "      <td>10.0</td>\n",
              "      <td>38.0</td>\n",
              "      <td>0.99735</td>\n",
              "      <td>3.31</td>\n",
              "      <td>0.64</td>\n",
              "      <td>9.40</td>\n",
              "      <td>5</td>\n",
              "      <td>red</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>6.8</td>\n",
              "      <td>0.370</td>\n",
              "      <td>0.51</td>\n",
              "      <td>11.8</td>\n",
              "      <td>0.044</td>\n",
              "      <td>62.0</td>\n",
              "      <td>163.0</td>\n",
              "      <td>0.99760</td>\n",
              "      <td>3.19</td>\n",
              "      <td>0.44</td>\n",
              "      <td>8.80</td>\n",
              "      <td>5</td>\n",
              "      <td>white</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>8.9</td>\n",
              "      <td>0.750</td>\n",
              "      <td>0.14</td>\n",
              "      <td>2.5</td>\n",
              "      <td>0.086</td>\n",
              "      <td>9.0</td>\n",
              "      <td>30.0</td>\n",
              "      <td>0.99824</td>\n",
              "      <td>3.34</td>\n",
              "      <td>0.64</td>\n",
              "      <td>10.50</td>\n",
              "      <td>5</td>\n",
              "      <td>red</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-46efddd7-4f95-4a18-8228-8526af474fe2')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-46efddd7-4f95-4a18-8228-8526af474fe2 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-46efddd7-4f95-4a18-8228-8526af474fe2');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-6810895c-8364-4eee-9c2a-af98130fe007\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-6810895c-8364-4eee-9c2a-af98130fe007')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-6810895c-8364-4eee-9c2a-af98130fe007 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ],
      "source": [
        "df.head()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "yeoPLe9BEOfG"
      },
      "source": [
        "Кількісний розподіл якості вина:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "XNE5y9EdEOfH",
        "outputId": "3f1bb280-669f-4180-b176-49f27065e27e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 391
        }
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 600x400 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAhEAAAF2CAYAAADQh8ptAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAq2ElEQVR4nO3dfXiT9b3H8U8a2tAiKU99lFIrKk+liKBQHxgKtGLliDIVRXGKeumKE6uIHLW0MMWxoXMOUee0ToHhdHoUkDbgEJEiD1IRcAgeWZ3YsiNCgGJIm/v8gQnENkB/pqSW9+u6cjX37/7ll2++V0I/3LnT2CzLsgQAANBIUZEuAAAA/DQRIgAAgBFCBAAAMEKIAAAARggRAADACCECAAAYIUQAAAAjhAgAAGCEEAEAAIwQIgA0C8uWLZPNZtOyZcsCY7/4xS902mmnRawmAEdHiADwk1FTU6OioqKgoAEgclpFugAACOVPf/qTfD5fYLumpkbFxcWSpMGDB0eoKgB+hAgAzVZ0dHSkSwBwFLydAaCeFStW6Nxzz1Xr1q3VtWtXPfvssyoqKpLNZpMkbd++XTabTSUlJfVua7PZVFRUFNj+17/+pV/+8pfq1q2bYmNj1bFjR1199dXavn37Mes48pyI7du3KyEhQZJUXFwsm80WuK8XX3xRNptN69evr7fGo48+Krvdrq+++qrRfQBwdByJABDkk08+UU5OjhISElRUVKTa2lpNmTJFSUlJRuutWbNGK1eu1OjRo9W5c2dt375ds2fP1uDBg7V582bFxcUd1zoJCQmaPXu27rzzTl155ZW66qqrJElZWVnKyMhQfn6+5syZo759+wbdbs6cORo8eLBOPfVUo/oBhEaIABCksLBQlmXp/fffV5cuXSRJo0aNUu/evY3Wy8vL089//vOgsREjRig7O1uvv/66brzxxuNap02bNvr5z3+uO++8U1lZWbrhhhuC9o8cOVLz5s3TjBkzFBV16CDr+vXrtXnzZk2cONGodgBHx9sZAALq6upUWlqqkSNHBgKEJPXo0UO5ublGa8bGxgaue71effPNNzrjjDPUrl07ffTRRz+6Zr+xY8dqx44d+sc//hEYmzNnjmJjYzVq1Kiw3Q+AwwgRAAL+85//6MCBAzrzzDPr7evWrZvRmgcOHFBhYaHS0tLkcDjUqVMnJSQkaPfu3dqzZ8+PLTlg2LBhSklJ0Zw5cyRJPp9P8+bN0xVXXKG2bduG7X4AHEaIANBo/hMsf6iurq7e2F133aVHHnlE11xzjV599VWVlZXJ5XKpY8eOQR/f/LHsdruuv/56vf766/ruu+/0j3/8Qzt27Kj3tgeA8OGcCAABCQkJio2N1datW+vt27JlS+B6+/btJUm7d+8OmvOvf/2r3u1ee+013XTTTZo5c2Zg7Lvvvqt32+MRKrz4jR07VjNnztTbb7+td955RwkJCcZvwwA4No5EAAiw2+3Kzc3Vm2++qcrKysD4p59+qtLS0sC20+lUp06dtHz58qDbP/300w2uaVlW0NhTTz3V4FGLY/F/kiNUAMnKylJWVpaef/55vf766xo9erRateL/SkBT4dUFIEhxcbEWL16siy66SL/85S9VW1urp556Sr169dKGDRsC82699VY99thjuvXWW9W/f38tX75cn332Wb31Lr/8cr388suKj49Xz549VV5eriVLlqhjx46Nri02NlY9e/bU/PnzddZZZ6lDhw7KzMxUZmZmYM7YsWN13333SRJvZQBNjCMRAIJkZWWptLRUCQkJKiws1AsvvKDi4mJdeeWVQfMKCws1btw4vfbaa7r//vtVV1end955p956Tz75pMaOHas5c+bo3nvv1ddff60lS5bolFNOMarv+eef16mnnqp77rlH1113nV577bWg/WPGjJHdbtdZZ52l8847z+g+ABwfm/XD44wA0ICioiIVFxfXe2uiufm///s/paSkqLCwUA8//HCkywFaNI5EAGhRSkpKVFdXd9x/xAqAOc6JANAivPvuu9q8ebMeeeQRjRw5MvCdGwCaDiECQIswdepUrVy5UhdccIGeeuqpSJcDnBQ4JwIAABjhnAgAAGCEEAEAAIy02HMifD6fduzYobZt2x7zT+UCAIDDLMvS3r17lZqaqqio0McbWmyI2LFjh9LS0iJdBgAAP1lffvmlOnfuHHJ/iw0R/q/+/fLLL+V0OsOyptfrVVlZmXJychQdHR2WNVsC+hIavWkYfQmN3jSMvoTWFL1xu91KS0sL/C4NpcWGCP9bGE6nM6whIi4uTk6nkyfxEehLaPSmYfQlNHrTMPoSWlP25linA3BiJQAAMEKIAAAARggRAADACCECAAAYIUQAAAAjhAgAAGCEEAEAAIwQIgAAgBFCBAAAMEKIAAAARggRAADACCECAAAYabFfwAWg+cssKpWn7vAX/Gx/LC+C1QBoLI5EAAAAI4QIAABghBABAACMECIAAIARQgQAADBCiAAAAEYIEQAAwAghAgAAGCFEAAAAI4QIAABghBABAACMECIAAIARQgQAADBCiAAAAEYIEQAAwAghAgAAGCFEAAAAI4QIAABghBABAACMECIAAIARQgQAADBCiAAAAEYIEQAAwAghAgAAGCFEAAAAI4QIAABghBABAACMECIAAIARQgQAADDSqBAxffp0nXvuuWrbtq0SExM1cuRIbdmyJWjO4MGDZbPZgi533HFH0JzKykrl5eUpLi5OiYmJmjhxompra4PmLFu2TOecc44cDofOOOMMlZSUmD1CAADQJBoVIt577z3l5+dr1apVcrlc8nq9ysnJ0f79+4Pm3Xbbbfr6668DlxkzZgT21dXVKS8vTwcPHtTKlSv10ksvqaSkRIWFhYE5X3zxhfLy8nTxxReroqJCEyZM0K233qrS0tIf+XABAEC4tGrM5MWLFwdtl5SUKDExUevWrdOgQYMC43FxcUpOTm5wjbKyMm3evFlLlixRUlKSzj77bE2bNk2TJk1SUVGRYmJi9MwzzygjI0MzZ86UJPXo0UMrVqzQE088odzc3MY+RgAA0AR+1DkRe/bskSR16NAhaHzOnDnq1KmTMjMzNXnyZNXU1AT2lZeXq3fv3kpKSgqM5ebmyu12a9OmTYE5Q4cODVozNzdX5eXlP6ZcAAAQRo06EnEkn8+nCRMm6IILLlBmZmZg/Prrr1d6erpSU1O1YcMGTZo0SVu2bNHf//53SVJVVVVQgJAU2K6qqjrqHLfbrQMHDig2NrZePR6PRx6PJ7DtdrslSV6vV16v1/RhBvGvE671Wgr6Ehq9aZi/H44oq8HxkxnPmYbRl9CaojfHu5ZxiMjPz9fGjRu1YsWKoPHbb789cL13795KSUnRkCFD9Pnnn6tr166md3dM06dPV3Fxcb3xsrIyxcXFhfW+XC5XWNdrKehLaPSmYdP6+4K2Fy1aFKFKmh+eMw2jL6GFszdHvoNwNEYhYvz48VqwYIGWL1+uzp07H3XugAEDJEnbtm1T165dlZycrNWrVwfNqa6ulqTAeRTJycmBsSPnOJ3OBo9CSNLkyZNVUFAQ2Ha73UpLS1NOTo6cTmfjHmAIXq9XLpdLw4YNU3R0dFjWbAnoS2j0pmH+vjy8Nkoeny0wvrGIc554zjSMvoTWFL3xH80/lkaFCMuydNddd+mNN97QsmXLlJGRcczbVFRUSJJSUlIkSdnZ2XrkkUe0c+dOJSYmSjqUnpxOp3r27BmY88P/kbhcLmVnZ4e8H4fDIYfDUW88Ojo67E+4plizJaAvodGbhnl8NnnqDocIenQYz5mG0ZfQwtmb412nUSdW5ufn65VXXtHcuXPVtm1bVVVVqaqqSgcOHJAkff7555o2bZrWrVun7du366233tLYsWM1aNAgZWVlSZJycnLUs2dP3Xjjjfr4449VWlqqhx56SPn5+YEQcMcdd+h///d/df/99+uf//ynnn76ab366qu65557GlMuAABoQo0KEbNnz9aePXs0ePBgpaSkBC7z58+XJMXExGjJkiXKyclR9+7dde+992rUqFF6++23A2vY7XYtWLBAdrtd2dnZuuGGGzR27FhNnTo1MCcjI0MLFy6Uy+VSnz59NHPmTD3//PN8vBMAgGak0W9nHE1aWpree++9Y66Tnp5+zBOoBg8erPXr1zemPAAAcALx3RkAAMAIIQIAABghRAAAACOECAAAYIQQAQAAjBAiAACAEUIEAAAwQogAAABGCBEAAMAIIQIAABghRAAAACOECAAAYIQQAQAAjBAiAACAEUIEAAAwQogAAABGCBEAAMAIIQIAABghRAAAACOECAAAYIQQAQAAjBAiAACAEUIEAAAwQogAAABGCBEAAMAIIQIAABghRAAAACOECAAAYIQQAQAAjBAiAACAEUIEAAAw0irSBQAt1WkPLJTDbmnGeVJmUak8dTZtfywv0mUBQNhwJAIAABghRAAAACOECAAAYIQQAQAAjBAiAACAEUIEAAAwQogAAABGCBEAAMAIIQIAABhpVIiYPn26zj33XLVt21aJiYkaOXKktmzZEjTnu+++U35+vjp27KhTTjlFo0aNUnV1ddCcyspK5eXlKS4uTomJiZo4caJqa2uD5ixbtkznnHOOHA6HzjjjDJWUlJg9QgAA0CQaFSLee+895efna9WqVXK5XPJ6vcrJydH+/fsDc+655x69/fbb+tvf/qb33ntPO3bs0FVXXRXYX1dXp7y8PB08eFArV67USy+9pJKSEhUWFgbmfPHFF8rLy9PFF1+siooKTZgwQbfeeqtKS0vD8JABAEA4NOq7MxYvXhy0XVJSosTERK1bt06DBg3Snj179Oc//1lz587VJZdcIkl68cUX1aNHD61atUoDBw5UWVmZNm/erCVLligpKUlnn322pk2bpkmTJqmoqEgxMTF65plnlJGRoZkzZ0qSevTooRUrVuiJJ55Qbm5umB46AAD4MX7UF3Dt2bNHktShQwdJ0rp16+T1ejV06NDAnO7du6tLly4qLy/XwIEDVV5ert69eyspKSkwJzc3V3feeac2bdqkvn37qry8PGgN/5wJEyaErMXj8cjj8QS23W63JMnr9crr9f6YhxngXydc67UU9KVhDrslR5R16Pr3P+nRIf4++Pvyw/GTGa+nhtGX0JqiN8e7lnGI8Pl8mjBhgi644AJlZmZKkqqqqhQTE6N27doFzU1KSlJVVVVgzpEBwr/fv+9oc9xutw4cOKDY2Nh69UyfPl3FxcX1xsvKyhQXF2f2IENwuVxhXa+loC/BZpx3+Pq0/j5J0qJFiyJUTfPk74sf/TmM11PD6Eto4exNTU3Ncc0zDhH5+fnauHGjVqxYYbpEWE2ePFkFBQWBbbfbrbS0NOXk5MjpdIblPrxer1wul4YNG6bo6OiwrNkS0JeGZRaVyhFlaVp/nx5eGyWPz6aNRbwdJx1+zvj74kd/eD2FQl9Ca4re+I/mH4tRiBg/frwWLFig5cuXq3PnzoHx5ORkHTx4ULt37w46GlFdXa3k5OTAnNWrVwet5//0xpFzfviJjurqajmdzgaPQkiSw+GQw+GoNx4dHR32J1xTrNkS0JdgnrrDvxw9Pps8dTb68wP+vvjRn8N4PTWMvoQWzt4c7zqN+nSGZVkaP3683njjDb377rvKyMgI2t+vXz9FR0dr6dKlgbEtW7aosrJS2dnZkqTs7Gx98skn2rlzZ2COy+WS0+lUz549A3OOXMM/x78GAACIvEYdicjPz9fcuXP1P//zP2rbtm3gHIb4+HjFxsYqPj5e48aNU0FBgTp06CCn06m77rpL2dnZGjhwoCQpJydHPXv21I033qgZM2aoqqpKDz30kPLz8wNHEu644w798Y9/1P33369bbrlF7777rl599VUtXLgwzA8fAACYatSRiNmzZ2vPnj0aPHiwUlJSApf58+cH5jzxxBO6/PLLNWrUKA0aNEjJycn6+9//Hthvt9u1YMEC2e12ZWdn64YbbtDYsWM1derUwJyMjAwtXLhQLpdLffr00cyZM/X888/z8U4AAJqRRh2JsCzrmHNat26tWbNmadasWSHnpKenH/Ms7MGDB2v9+vWNKQ8AAJxAfHcGAAAwQogAAABGCBEAAMAIIQIAABghRAAAACOECAAAYIQQAQAAjBAiAACAEUIEAAAwQogAAABGCBEAAMAIIQIAABghRAAAACOECAAAYIQQAQAAjBAiAACAEUIEAAAwQogAAABGCBEAAMAIIQIAABghRAAAACOECAAAYIQQAQAAjBAiAACAEUIEAAAwQogAAABGCBEAAMAIIQIAABghRAAAACOECAAAYIQQAQAAjBAiAACAEUIEAAAwQogAAABGCBEAAMAIIQIAABghRAAAACOECAAAYIQQAQAAjBAiAACAEUIEAAAw0ugQsXz5co0YMUKpqamy2Wx68803g/b/4he/kM1mC7pceumlQXN27dqlMWPGyOl0ql27dho3bpz27dsXNGfDhg266KKL1Lp1a6WlpWnGjBmNf3QAAKDJNDpE7N+/X3369NGsWbNCzrn00kv19ddfBy7z5s0L2j9mzBht2rRJLpdLCxYs0PLly3X77bcH9rvdbuXk5Cg9PV3r1q3Tb3/7WxUVFem5555rbLkAAKCJtGrsDYYPH67hw4cfdY7D4VBycnKD+z799FMtXrxYa9asUf/+/SVJTz31lC677DL97ne/U2pqqubMmaODBw/qhRdeUExMjHr16qWKigo9/vjjQWEDAABETqNDxPFYtmyZEhMT1b59e11yySX69a9/rY4dO0qSysvL1a5du0CAkKShQ4cqKipKH374oa688kqVl5dr0KBBiomJCczJzc3Vb37zG3377bdq3759vfv0eDzyeDyBbbfbLUnyer3yer1heVz+dcK1XktBXxrmsFtyRFmHrn//kx4d4u+Dvy8/HD+Z8XpqGH0JrSl6c7xrhT1EXHrppbrqqquUkZGhzz//XP/93/+t4cOHq7y8XHa7XVVVVUpMTAwuolUrdejQQVVVVZKkqqoqZWRkBM1JSkoK7GsoREyfPl3FxcX1xsvKyhQXFxeuhydJcrlcYV2vpaAvwWacd/j6tP4+SdKiRYsiVE3z5O+LH/05jNdTw+hLaOHsTU1NzXHNC3uIGD16dOB67969lZWVpa5du2rZsmUaMmRIuO8uYPLkySooKAhsu91upaWlKScnR06nMyz34fV65XK5NGzYMEVHR4dlzZaAvjQss6hUjihL0/r79PDaKHl8Nm0syo10Wc2C/znj74sf/eH1FAp9Ca0peuM/mn8sTfJ2xpFOP/10derUSdu2bdOQIUOUnJysnTt3Bs2pra3Vrl27AudRJCcnq7q6OmiOfzvUuRYOh0MOh6PeeHR0dNifcE2xZktAX4J56g7/cvT4bPLU2ejPD/j74kd/DuP11DD6Elo4e3O86zT534n497//rW+++UYpKSmSpOzsbO3evVvr1q0LzHn33Xfl8/k0YMCAwJzly5cHvSfjcrnUrVu3Bt/KAAAAJ16jQ8S+fftUUVGhiooKSdIXX3yhiooKVVZWat++fZo4caJWrVql7du3a+nSpbriiit0xhlnKDf30GHKHj166NJLL9Vtt92m1atX64MPPtD48eM1evRopaamSpKuv/56xcTEaNy4cdq0aZPmz5+vJ598MujtCgAAEFmNDhFr165V37591bdvX0lSQUGB+vbtq8LCQtntdm3YsEH/9V//pbPOOkvjxo1Tv3799P777we91TBnzhx1795dQ4YM0WWXXaYLL7ww6G9AxMfHq6ysTF988YX69eune++9V4WFhXy8EwCAZqTR50QMHjxYlmWF3F9aWnrMNTp06KC5c+cedU5WVpbef//9xpYHAABOEL47AwAAGCFEAAAAI4QIAABghBABAACMECIAAIARQgQAADBCiAAAAEYIEQAAwAghAgAAGCFEAAAAI4QIAABghBABAACMECIAAIARQgQAADBCiAAAAEYIEQAAwAghAgAAGCFEAAAAI4QIAABghBABAACMECIAAIARQgQAADBCiAAAAEYIEQAAwAghAgAAGCFEAAAAI4QIAABghBABAACMECIAAIARQgQAADBCiAAAAEYIEQAAwAghAgAAGCFEAAAAI4QIAABghBABAACMECIAAICRVpEuAAAgnfbAQkmSw25pxnkRLgY4ThyJAAAARggRAADASKNDxPLlyzVixAilpqbKZrPpzTffDNpvWZYKCwuVkpKi2NhYDR06VFu3bg2as2vXLo0ZM0ZOp1Pt2rXTuHHjtG/fvqA5GzZs0EUXXaTWrVsrLS1NM2bMaPyjAwAATabRIWL//v3q06ePZs2a1eD+GTNm6A9/+IOeeeYZffjhh2rTpo1yc3P13XffBeaMGTNGmzZtksvl0oIFC7R8+XLdfvvtgf1ut1s5OTlKT0/XunXr9Nvf/lZFRUV67rnnDB4iAABoCo0+sXL48OEaPnx4g/ssy9Lvf/97PfTQQ7riiiskSX/5y1+UlJSkN998U6NHj9ann36qxYsXa82aNerfv78k6amnntJll12m3/3ud0pNTdWcOXN08OBBvfDCC4qJiVGvXr1UUVGhxx9/PChsAACAyAnrORFffPGFqqqqNHTo0MBYfHy8BgwYoPLycklSeXm52rVrFwgQkjR06FBFRUXpww8/DMwZNGiQYmJiAnNyc3O1ZcsWffvtt+EsGQAAGArrRzyrqqokSUlJSUHjSUlJgX1VVVVKTEwMLqJVK3Xo0CFoTkZGRr01/Pvat29f7749Ho88Hk9g2+12S5K8Xq+8Xu+PeVgB/nXCtV5LQV8a5rBbckRZh65//5MeHeLvg78vPxw/GTnsPFeOhn9nQmuK3hzvWi3m70RMnz5dxcXF9cbLysoUFxcX1vtyuVxhXa+loC/Bjvys/7T+PknSokWLIlRN8+Tvi9/J3J8f/m0IXk8Noy+hhbM3NTU1xzUvrCEiOTlZklRdXa2UlJTAeHV1tc4+++zAnJ07dwbdrra2Vrt27QrcPjk5WdXV1UFz/Nv+OT80efJkFRQUBLbdbrfS0tKUk5Mjp9P54x7Y97xer1wul4YNG6bo6OiwrNkS0JeGZRaVyhFlaVp/nx5eGyWPz6aNRbmRLqtZ8D9n/H3xO5n7k1lUKkmB5wyvp2D8OxNaU/TGfzT/WMIaIjIyMpScnKylS5cGQoPb7daHH36oO++8U5KUnZ2t3bt3a926derXr58k6d1335XP59OAAQMCcx588EF5vd5AQ1wul7p169bgWxmS5HA45HA46o1HR0eH/QnXFGu2BPQlmKfu8C9Hj88mT52N/vyAvy9+J3N/juyDxOspFPoSWjh7c7zrNPrEyn379qmiokIVFRWSDp1MWVFRocrKStlsNk2YMEG//vWv9dZbb+mTTz7R2LFjlZqaqpEjR0qSevTooUsvvVS33XabVq9erQ8++EDjx4/X6NGjlZqaKkm6/vrrFRMTo3HjxmnTpk2aP3++nnzyyaAjDQAAILIafSRi7dq1uvjiiwPb/l/sN910k0pKSnT//fdr//79uv3227V7925deOGFWrx4sVq3bh24zZw5czR+/HgNGTJEUVFRGjVqlP7whz8E9sfHx6usrEz5+fnq16+fOnXqpMLCQj7eCQBAM9LoEDF48GBZlhVyv81m09SpUzV16tSQczp06KC5c+ce9X6ysrL0/vvvN7Y8AABwgvDdGQAAwAghAgAAGCFEAAAAI4QIAABghBABAACMECIAAIARQgQAADBCiAAAAEYIEQAAwAghAgAAGCFEAAAAI4QIAABghBABAACMECIAAIARQgQAADBCiAAAAEYIEQAAwAghAgAAGCFEAAAAI4QIAABghBABAACMECIAAIARQgQAADBCiAAAAEYIEQAAwAghAgAAGCFEAAAAI4QIAABghBABAACMECIAAIARQgQAADBCiAAAAEYIEQAAwAghAgAAGCFEAAAAI4QIAABghBABAACMECIAAIARQgQAADBCiAAAAEYIEQAAwEjYQ0RRUZFsNlvQpXv37oH93333nfLz89WxY0edcsopGjVqlKqrq4PWqKysVF5enuLi4pSYmKiJEyeqtrY23KUCAIAfoVVTLNqrVy8tWbLk8J20Onw399xzjxYuXKi//e1vio+P1/jx43XVVVfpgw8+kCTV1dUpLy9PycnJWrlypb7++muNHTtW0dHRevTRR5uiXAAAYKBJQkSrVq2UnJxcb3zPnj3685//rLlz5+qSSy6RJL344ovq0aOHVq1apYEDB6qsrEybN2/WkiVLlJSUpLPPPlvTpk3TpEmTVFRUpJiYmKYoGQAANFKTnBOxdetWpaam6vTTT9eYMWNUWVkpSVq3bp28Xq+GDh0amNu9e3d16dJF5eXlkqTy8nL17t1bSUlJgTm5ublyu93atGlTU5QLAAAMhP1IxIABA1RSUqJu3brp66+/VnFxsS666CJt3LhRVVVViomJUbt27YJuk5SUpKqqKklSVVVVUIDw7/fvC8Xj8cjj8QS23W63JMnr9crr9YbjoQXWCdd6LQV9aZjDbskRZR26/v1PenSIvw/+vvxw/GTksPNcORr+nQmtKXpzvGuFPUQMHz48cD0rK0sDBgxQenq6Xn31VcXGxob77gKmT5+u4uLieuNlZWWKi4sL6325XK6wrtdS0JdgM847fH1af58kadGiRRGqpnny98XvZO7Pkc8XiddTKPQltHD2pqam5rjmNck5EUdq166dzjrrLG3btk3Dhg3TwYMHtXv37qCjEdXV1YFzKJKTk7V69eqgNfyf3mjoPAu/yZMnq6CgILDtdruVlpamnJwcOZ3OsDwWr9crl8ulYcOGKTo6OixrtgT0pWGZRaVyRFma1t+nh9dGyeOzaWNRbqTLahb8zxl/X/xO5v5kFpVKUuA5w+spGP/OhNYUvfEfzT+WJg8R+/bt0+eff64bb7xR/fr1U3R0tJYuXapRo0ZJkrZs2aLKykplZ2dLkrKzs/XII49o586dSkxMlHQoXTmdTvXs2TPk/TgcDjkcjnrj0dHRYX/CNcWaLQF9CeapO/zL0eOzyVNnoz8/4O+L38ncnyP7IPF6CoW+hBbO3hzvOmEPEffdd59GjBih9PR07dixQ1OmTJHdbtd1112n+Ph4jRs3TgUFBerQoYOcTqfuuusuZWdna+DAgZKknJwc9ezZUzfeeKNmzJihqqoqPfTQQ8rPz28wJAAAgMgIe4j497//reuuu07ffPONEhISdOGFF2rVqlVKSEiQJD3xxBOKiorSqFGj5PF4lJubq6effjpwe7vdrgULFujOO+9Udna22rRpo5tuuklTp04Nd6kAAOBHCHuI+Otf/3rU/a1bt9asWbM0a9askHPS09NP6hOsAAD4KeC7MwAAgBFCBAAAMEKIAAAARggRAADACCECAAAYIUQAAAAjhAgAAGCEEAEAAIwQIgAAgBFCBAAAMEKIAAAARggRAADACCECAAAYIUQAAAAjhAgAAGCEEAEAAIwQIgAAgBFCBAAAMEKIAAAARggRAADACCECAAAYIUQAAAAjhAgAAGCEEIEf5bQHFiqzqFSSAj8BACcHQgQAADBCiAAANHtHHvE87YGFEa4GfoQIAABghBABAACMECIAAIARQgQAADBCiAAAAEYIEQAAwAghAgAAGCFEAAAAI4QIAABghBABAACMECIAAIARQgQAADBCiAAAAEYIEQAAwAghAgAAGGnWIWLWrFk67bTT1Lp1aw0YMECrV6+OdEkAAOB7zTZEzJ8/XwUFBZoyZYo++ugj9enTR7m5udq5c2ekS1NmUalOe2ChTntgYaRLAQAgYpptiHj88cd122236eabb1bPnj31zDPPKC4uTi+88EKkSwMAAJJaRbqAhhw8eFDr1q3T5MmTA2NRUVEaOnSoysvLG7yNx+ORx+MJbO/Zs0eStGvXLnm93rDU5fV6VVNTo1beKNX5bJKkb775Jixr/1S1qt2vVj5LNTU+tfJGnfT9ONIPe1Pns9Gf7zX0WpJO7tdTq9r9h35+/5z55ptvFB0dHeGqmo9W3v28lkLwv57C+ZzZu3evJMmyrKNPtJqhr776ypJkrVy5Mmh84sSJ1nnnndfgbaZMmWJJ4sKFCxcuXLiE6fLll18e9fd1szwSYWLy5MkqKCgIbPt8Pu3atUsdO3aUzWY7yi2Pn9vtVlpamr788ks5nc6wrNkS0JfQ6E3D6Eto9KZh9CW0puiNZVnau3evUlNTjzqvWYaITp06yW63q7q6Omi8urpaycnJDd7G4XDI4XAEjbVr165J6nM6nTyJG0BfQqM3DaMvodGbhtGX0MLdm/j4+GPOaZYnVsbExKhfv35aunRpYMzn82np0qXKzs6OYGUAAMCvWR6JkKSCggLddNNN6t+/v8477zz9/ve/1/79+3XzzTdHujQAAKBmHCKuvfZa/ec//1FhYaGqqqp09tlna/HixUpKSopYTQ6HQ1OmTKn3tsnJjr6ERm8aRl9CozcNoy+hRbI3Nss61uc3AAAA6muW50QAAIDmjxABAACMECIAAIARQgQAADBCiDgOs2fPVlZWVuAPeWRnZ+udd96JdFnNzmOPPSabzaYJEyZEupSIKyoqks1mC7p079490mU1C1999ZVuuOEGdezYUbGxserdu7fWrl0b6bIi7rTTTqv3nLHZbMrPz490aRFVV1enhx9+WBkZGYqNjVXXrl01bdq0Y3+nw0lg7969mjBhgtLT0xUbG6vzzz9fa9asOaE1NNuPeDYnnTt31mOPPaYzzzxTlmXppZde0hVXXKH169erV69ekS6vWVizZo2effZZZWVlRbqUZqNXr15asmRJYLtVK15u3377rS644AJdfPHFeuedd5SQkKCtW7eqffv2kS4t4tasWaO6urrA9saNGzVs2DBdffXVEawq8n7zm99o9uzZeumll9SrVy+tXbtWN998s+Lj4/WrX/0q0uVF1K233qqNGzfq5ZdfVmpqql555RUNHTpUmzdv1qmnnnpiigjHF2adjNq3b289//zzkS6jWdi7d6915plnWi6Xy/rZz35m3X333ZEuKeKmTJli9enTJ9JlNDuTJk2yLrzwwkiX8ZNw9913W127drV8Pl+kS4movLw865Zbbgkau+qqq6wxY8ZEqKLmoaamxrLb7daCBQuCxs855xzrwQcfPGF18HZGI9XV1emvf/2r9u/fz5/g/l5+fr7y8vI0dOjQSJfSrGzdulWpqak6/fTTNWbMGFVWVka6pIh766231L9/f1199dVKTExU37599ac//SnSZTU7Bw8e1CuvvKJbbrklbF8g+FN1/vnna+nSpfrss88kSR9//LFWrFih4cOHR7iyyKqtrVVdXZ1at24dNB4bG6sVK1acuEJOWFz5iduwYYPVpk0by263W/Hx8dbChQsjXVKzMG/ePCszM9M6cOCAZVkWRyK+t2jRIuvVV1+1Pv74Y2vx4sVWdna21aVLF8vtdke6tIhyOByWw+GwJk+ebH300UfWs88+a7Vu3doqKSmJdGnNyvz58y273W599dVXkS4l4urq6qxJkyZZNpvNatWqlWWz2axHH3000mU1C9nZ2dbPfvYz66uvvrJqa2utl19+2YqKirLOOuusE1YDIeI4eTwea+vWrdbatWutBx54wOrUqZO1adOmSJcVUZWVlVZiYqL18ccfB8YIEQ379ttvLafTedK/BRYdHW1lZ2cHjd11113WwIEDI1RR85STk2NdfvnlkS6jWZg3b57VuXNna968edaGDRusv/zlL1aHDh0InpZlbdu2zRo0aJAlybLb7da5555rjRkzxurevfsJq4EQYWjIkCHW7bffHukyIuqNN94IPHn9F0mWzWaz7Ha7VVtbG+kSm5X+/ftbDzzwQKTLiKguXbpY48aNCxp7+umnrdTU1AhV1Pxs377dioqKst58881Il9IsdO7c2frjH/8YNDZt2jSrW7duEaqo+dm3b5+1Y8cOy7Is65prrrEuu+yyE3bfnBNhyOfzyePxRLqMiBoyZIg++eQTVVRUBC79+/fXmDFjVFFRIbvdHukSm419+/bp888/V0pKSqRLiagLLrhAW7ZsCRr77LPPlJ6eHqGKmp8XX3xRiYmJysvLi3QpzUJNTY2iooJ/Vdntdvl8vghV1Py0adNGKSkp+vbbb1VaWqorrrjihN03nzk7DpMnT9bw4cPVpUsX7d27V3PnztWyZctUWloa6dIiqm3btsrMzAwaa9OmjTp27Fhv/GRz3333acSIEUpPT9eOHTs0ZcoU2e12XXfddZEuLaLuuecenX/++Xr00Ud1zTXXaPXq1Xruuef03HPPRbq0ZsHn8+nFF1/UTTfdxEeCvzdixAg98sgj6tKli3r16qX169fr8ccf1y233BLp0iKutLRUlmWpW7du2rZtmyZOnKju3bvr5ptvPnFFnLBjHj9ht9xyi5Wenm7FxMRYCQkJ1pAhQ6yysrJIl9UscU7EIddee62VkpJixcTEWKeeeqp17bXXWtu2bYt0Wc3C22+/bWVmZloOh8Pq3r279dxzz0W6pGajtLTUkmRt2bIl0qU0G26327r77rutLl26WK1bt7ZOP/1068EHH7Q8Hk+kS4u4+fPnW6effroVExNjJScnW/n5+dbu3btPaA18FTgAADDCOREAAMAIIQIAABghRAAAACOECAAAYIQQAQAAjBAiAACAEUIEAAAwQogAAABGCBEAAMAIIQIAABghRAAAACOECAAAYOT/AWoJPtWbijIOAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "df.hist('quality', bins=100, figsize=(6, 4));"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "a5f9_mXnEOfI"
      },
      "source": [
        "Додамо колонку \"клас\" для подальшої класифікації:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "FnvBokkGEOfI"
      },
      "outputs": [],
      "source": [
        "df['class'] = df.quality.apply(lambda x: \"high\" if x > 6 else \"low\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sk-ksWhKEOfJ"
      },
      "source": [
        "Візуалізація багатовимірних зв’язків між зразками:\n",
        "\n",
        "> Примітка: візуалізація може зайняти 1-2 хвилини"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "AP9__LQ1EOfJ",
        "outputId": "47971cce-30c9-4613-bdf3-f52db866db63",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        }
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 2830.25x2750 with 132 Axes>"
            ],
          },
          "metadata": {}
        }
      ],
      "source": [
        "sns.pairplot(df.drop('quality', axis=1), hue='class', height=2.5);"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "yvXZ_vW-EOfK"
      },
      "source": [
        "Як видно, багато фіч є корельованими, що також можна побачити за допомогою матриці кореляції:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "HS8I5SA5EOfK",
        "outputId": "91cd9381-9fd4-43e1-94f6-2b299d9cea2f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 425
        }
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pandas.io.formats.style.Styler at 0x7d866615ef20>"
            ],
            "text/html": [
              "<style type=\"text/css\">\n",
              "#T_c2f8a_row0_col0, #T_c2f8a_row1_col1, #T_c2f8a_row2_col2, #T_c2f8a_row3_col3, #T_c2f8a_row4_col4, #T_c2f8a_row5_col5, #T_c2f8a_row6_col6, #T_c2f8a_row7_col7, #T_c2f8a_row8_col8, #T_c2f8a_row9_col9, #T_c2f8a_row10_col10, #T_c2f8a_row11_col11 {\n",
              "  background-color: #ff0000;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row0_col1, #T_c2f8a_row1_col0, #T_c2f8a_row1_col9, #T_c2f8a_row9_col1 {\n",
              "  background-color: #ffc6c6;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row0_col2, #T_c2f8a_row2_col0 {\n",
              "  background-color: #ffacac;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row0_col3 {\n",
              "  background-color: #a8a8ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row0_col4, #T_c2f8a_row0_col9, #T_c2f8a_row4_col0, #T_c2f8a_row9_col0 {\n",
              "  background-color: #ffb2b2;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row0_col5 {\n",
              "  background-color: #2424ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row0_col6, #T_c2f8a_row1_col6, #T_c2f8a_row2_col1, #T_c2f8a_row3_col10, #T_c2f8a_row4_col6, #T_c2f8a_row5_col1, #T_c2f8a_row6_col1, #T_c2f8a_row7_col10, #T_c2f8a_row8_col2, #T_c2f8a_row9_col6, #T_c2f8a_row10_col3, #T_c2f8a_row11_col1 {\n",
              "  background-color: #0000ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row0_col7, #T_c2f8a_row7_col0 {\n",
              "  background-color: #ffb4b4;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row0_col8, #T_c2f8a_row8_col0 {\n",
              "  background-color: #3a3aff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row0_col10 {\n",
              "  background-color: #b4b4ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row0_col11 {\n",
              "  background-color: #c4c4ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row1_col2 {\n",
              "  background-color: #1616ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row1_col3 {\n",
              "  background-color: #8686ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row1_col4, #T_c2f8a_row4_col1 {\n",
              "  background-color: #ff9e9e;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row1_col5 {\n",
              "  background-color: #2626ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row1_col7, #T_c2f8a_row2_col9, #T_c2f8a_row5_col11, #T_c2f8a_row7_col1, #T_c2f8a_row9_col2, #T_c2f8a_row11_col5 {\n",
              "  background-color: #fff0f0;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row1_col8, #T_c2f8a_row8_col1 {\n",
              "  background-color: #ffbcbc;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row1_col10 {\n",
              "  background-color: #e8e8ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row1_col11, #T_c2f8a_row6_col10 {\n",
              "  background-color: #5a5aff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row2_col3, #T_c2f8a_row3_col2 {\n",
              "  background-color: #ffdada;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row2_col4, #T_c2f8a_row4_col2, #T_c2f8a_row9_col11, #T_c2f8a_row11_col9 {\n",
              "  background-color: #fff6f6;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row2_col5, #T_c2f8a_row5_col2 {\n",
              "  background-color: #ffdcdc;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row2_col6, #T_c2f8a_row6_col2, #T_c2f8a_row8_col9, #T_c2f8a_row9_col8 {\n",
              "  background-color: #ffcece;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row2_col7, #T_c2f8a_row7_col2 {\n",
              "  background-color: #ffdede;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row2_col8 {\n",
              "  background-color: #2020ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row2_col10, #T_c2f8a_row7_col6, #T_c2f8a_row10_col2 {\n",
              "  background-color: #f8f8ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row2_col11, #T_c2f8a_row11_col2 {\n",
              "  background-color: #ffeaea;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row3_col0 {\n",
              "  background-color: #b0b0ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row3_col1 {\n",
              "  background-color: #7474ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row3_col4 {\n",
              "  background-color: #a4a4ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row3_col5, #T_c2f8a_row5_col3 {\n",
              "  background-color: #ff9898;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row3_col6, #T_c2f8a_row6_col3 {\n",
              "  background-color: #ff8080;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row3_col7, #T_c2f8a_row7_col3 {\n",
              "  background-color: #ffd2d2;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row3_col8 {\n",
              "  background-color: #4040ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row3_col9 {\n",
              "  background-color: #7a7aff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row3_col11, #T_c2f8a_row10_col1 {\n",
              "  background-color: #e4e4ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row4_col3 {\n",
              "  background-color: #8888ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row4_col5 {\n",
              "  background-color: #4c4cff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row4_col7, #T_c2f8a_row7_col4 {\n",
              "  background-color: #ffe6e6;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row4_col8, #T_c2f8a_row8_col4 {\n",
              "  background-color: #fff4f4;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row4_col9, #T_c2f8a_row9_col4 {\n",
              "  background-color: #ff9a9a;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row4_col10 {\n",
              "  background-color: #1414ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row4_col11, #T_c2f8a_row10_col4 {\n",
              "  background-color: #4848ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row5_col0 {\n",
              "  background-color: #3232ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row5_col4 {\n",
              "  background-color: #7272ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row5_col6, #T_c2f8a_row6_col5 {\n",
              "  background-color: #ff4646;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row5_col7 {\n",
              "  background-color: #f6f6ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row5_col8 {\n",
              "  background-color: #9696ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row5_col9 {\n",
              "  background-color: #7676ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row5_col10 {\n",
              "  background-color: #7c7cff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row6_col0 {\n",
              "  background-color: #3434ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row6_col4, #T_c2f8a_row9_col3 {\n",
              "  background-color: #5252ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row6_col7, #T_c2f8a_row9_col10, #T_c2f8a_row10_col9 {\n",
              "  background-color: #fcfcff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row6_col8 {\n",
              "  background-color: #6c6cff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row6_col9 {\n",
              "  background-color: #5454ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row6_col11 {\n",
              "  background-color: #e6e6ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row7_col5, #T_c2f8a_row8_col7 {\n",
              "  background-color: #ececff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row7_col8, #T_c2f8a_row11_col6 {\n",
              "  background-color: #d8d8ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row7_col9, #T_c2f8a_row9_col7 {\n",
              "  background-color: #ffe2e2;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row7_col11 {\n",
              "  background-color: #9a9aff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row8_col3 {\n",
              "  background-color: #3030ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row8_col5 {\n",
              "  background-color: #8e8eff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row8_col6 {\n",
              "  background-color: #4646ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row8_col10, #T_c2f8a_row10_col8 {\n",
              "  background-color: #ffe0e0;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row8_col11, #T_c2f8a_row11_col8 {\n",
              "  background-color: #fffafa;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row9_col5 {\n",
              "  background-color: #5050ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row10_col0 {\n",
              "  background-color: #bcbcff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row10_col5 {\n",
              "  background-color: #7e7eff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row10_col6 {\n",
              "  background-color: #4242ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row10_col7 {\n",
              "  background-color: #8a8aff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row10_col11, #T_c2f8a_row11_col10 {\n",
              "  background-color: #ff8e8e;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row11_col0 {\n",
              "  background-color: #b6b6ff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row11_col3 {\n",
              "  background-color: #dcdcff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row11_col4 {\n",
              "  background-color: #3e3eff;\n",
              "  color: black;\n",
              "}\n",
              "#T_c2f8a_row11_col7 {\n",
              "  background-color: #c2c2ff;\n",
              "  color: black;\n",
              "}\n",
              "</style>\n",
              "<table id=\"T_c2f8a\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr>\n",
              "      <th class=\"blank level0\" >&nbsp;</th>\n",
              "      <th id=\"T_c2f8a_level0_col0\" class=\"col_heading level0 col0\" >fixed acidity</th>\n",
              "      <th id=\"T_c2f8a_level0_col1\" class=\"col_heading level0 col1\" >volatile acidity</th>\n",
              "      <th id=\"T_c2f8a_level0_col2\" class=\"col_heading level0 col2\" >citric acid</th>\n",
              "      <th id=\"T_c2f8a_level0_col3\" class=\"col_heading level0 col3\" >residual sugar</th>\n",
              "      <th id=\"T_c2f8a_level0_col4\" class=\"col_heading level0 col4\" >chlorides</th>\n",
              "      <th id=\"T_c2f8a_level0_col5\" class=\"col_heading level0 col5\" >free sulfur dioxide</th>\n",
              "      <th id=\"T_c2f8a_level0_col6\" class=\"col_heading level0 col6\" >total sulfur dioxide</th>\n",
              "      <th id=\"T_c2f8a_level0_col7\" class=\"col_heading level0 col7\" >density</th>\n",
              "      <th id=\"T_c2f8a_level0_col8\" class=\"col_heading level0 col8\" >pH</th>\n",
              "      <th id=\"T_c2f8a_level0_col9\" class=\"col_heading level0 col9\" >sulphates</th>\n",
              "      <th id=\"T_c2f8a_level0_col10\" class=\"col_heading level0 col10\" >alcohol</th>\n",
              "      <th id=\"T_c2f8a_level0_col11\" class=\"col_heading level0 col11\" >quality</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th id=\"T_c2f8a_level0_row0\" class=\"row_heading level0 row0\" >fixed acidity</th>\n",
              "      <td id=\"T_c2f8a_row0_col0\" class=\"data row0 col0\" >1.00</td>\n",
              "      <td id=\"T_c2f8a_row0_col1\" class=\"data row0 col1\" >0.22</td>\n",
              "      <td id=\"T_c2f8a_row0_col2\" class=\"data row0 col2\" >0.32</td>\n",
              "      <td id=\"T_c2f8a_row0_col3\" class=\"data row0 col3\" >-0.11</td>\n",
              "      <td id=\"T_c2f8a_row0_col4\" class=\"data row0 col4\" >0.30</td>\n",
              "      <td id=\"T_c2f8a_row0_col5\" class=\"data row0 col5\" >-0.28</td>\n",
              "      <td id=\"T_c2f8a_row0_col6\" class=\"data row0 col6\" >-0.33</td>\n",
              "      <td id=\"T_c2f8a_row0_col7\" class=\"data row0 col7\" >0.29</td>\n",
              "      <td id=\"T_c2f8a_row0_col8\" class=\"data row0 col8\" >-0.25</td>\n",
              "      <td id=\"T_c2f8a_row0_col9\" class=\"data row0 col9\" >0.30</td>\n",
              "      <td id=\"T_c2f8a_row0_col10\" class=\"data row0 col10\" >-0.10</td>\n",
              "      <td id=\"T_c2f8a_row0_col11\" class=\"data row0 col11\" >-0.08</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th id=\"T_c2f8a_level0_row1\" class=\"row_heading level0 row1\" >volatile acidity</th>\n",
              "      <td id=\"T_c2f8a_row1_col0\" class=\"data row1 col0\" >0.22</td>\n",
              "      <td id=\"T_c2f8a_row1_col1\" class=\"data row1 col1\" >1.00</td>\n",
              "      <td id=\"T_c2f8a_row1_col2\" class=\"data row1 col2\" >-0.38</td>\n",
              "      <td id=\"T_c2f8a_row1_col3\" class=\"data row1 col3\" >-0.20</td>\n",
              "      <td id=\"T_c2f8a_row1_col4\" class=\"data row1 col4\" >0.38</td>\n",
              "      <td id=\"T_c2f8a_row1_col5\" class=\"data row1 col5\" >-0.35</td>\n",
              "      <td id=\"T_c2f8a_row1_col6\" class=\"data row1 col6\" >-0.41</td>\n",
              "      <td id=\"T_c2f8a_row1_col7\" class=\"data row1 col7\" >0.06</td>\n",
              "      <td id=\"T_c2f8a_row1_col8\" class=\"data row1 col8\" >0.26</td>\n",
              "      <td id=\"T_c2f8a_row1_col9\" class=\"data row1 col9\" >0.23</td>\n",
              "      <td id=\"T_c2f8a_row1_col10\" class=\"data row1 col10\" >-0.04</td>\n",
              "      <td id=\"T_c2f8a_row1_col11\" class=\"data row1 col11\" >-0.27</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th id=\"T_c2f8a_level0_row2\" class=\"row_heading level0 row2\" >citric acid</th>\n",
              "      <td id=\"T_c2f8a_row2_col0\" class=\"data row2 col0\" >0.32</td>\n",
              "      <td id=\"T_c2f8a_row2_col1\" class=\"data row2 col1\" >-0.38</td>\n",
              "      <td id=\"T_c2f8a_row2_col2\" class=\"data row2 col2\" >1.00</td>\n",
              "      <td id=\"T_c2f8a_row2_col3\" class=\"data row2 col3\" >0.14</td>\n",
              "      <td id=\"T_c2f8a_row2_col4\" class=\"data row2 col4\" >0.04</td>\n",
              "      <td id=\"T_c2f8a_row2_col5\" class=\"data row2 col5\" >0.13</td>\n",
              "      <td id=\"T_c2f8a_row2_col6\" class=\"data row2 col6\" >0.20</td>\n",
              "      <td id=\"T_c2f8a_row2_col7\" class=\"data row2 col7\" >0.13</td>\n",
              "      <td id=\"T_c2f8a_row2_col8\" class=\"data row2 col8\" >-0.33</td>\n",
              "      <td id=\"T_c2f8a_row2_col9\" class=\"data row2 col9\" >0.06</td>\n",
              "      <td id=\"T_c2f8a_row2_col10\" class=\"data row2 col10\" >-0.01</td>\n",
              "      <td id=\"T_c2f8a_row2_col11\" class=\"data row2 col11\" >0.09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th id=\"T_c2f8a_level0_row3\" class=\"row_heading level0 row3\" >residual sugar</th>\n",
              "      <td id=\"T_c2f8a_row3_col0\" class=\"data row3 col0\" >-0.11</td>\n",
              "      <td id=\"T_c2f8a_row3_col1\" class=\"data row3 col1\" >-0.20</td>\n",
              "      <td id=\"T_c2f8a_row3_col2\" class=\"data row3 col2\" >0.14</td>\n",
              "      <td id=\"T_c2f8a_row3_col3\" class=\"data row3 col3\" >1.00</td>\n",
              "      <td id=\"T_c2f8a_row3_col4\" class=\"data row3 col4\" >-0.13</td>\n",
              "      <td id=\"T_c2f8a_row3_col5\" class=\"data row3 col5\" >0.40</td>\n",
              "      <td id=\"T_c2f8a_row3_col6\" class=\"data row3 col6\" >0.50</td>\n",
              "      <td id=\"T_c2f8a_row3_col7\" class=\"data row3 col7\" >0.18</td>\n",
              "      <td id=\"T_c2f8a_row3_col8\" class=\"data row3 col8\" >-0.27</td>\n",
              "      <td id=\"T_c2f8a_row3_col9\" class=\"data row3 col9\" >-0.19</td>\n",
              "      <td id=\"T_c2f8a_row3_col10\" class=\"data row3 col10\" >-0.36</td>\n",
              "      <td id=\"T_c2f8a_row3_col11\" class=\"data row3 col11\" >-0.04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th id=\"T_c2f8a_level0_row4\" class=\"row_heading level0 row4\" >chlorides</th>\n",
              "      <td id=\"T_c2f8a_row4_col0\" class=\"data row4 col0\" >0.30</td>\n",
              "      <td id=\"T_c2f8a_row4_col1\" class=\"data row4 col1\" >0.38</td>\n",
              "      <td id=\"T_c2f8a_row4_col2\" class=\"data row4 col2\" >0.04</td>\n",
              "      <td id=\"T_c2f8a_row4_col3\" class=\"data row4 col3\" >-0.13</td>\n",
              "      <td id=\"T_c2f8a_row4_col4\" class=\"data row4 col4\" >1.00</td>\n",
              "      <td id=\"T_c2f8a_row4_col5\" class=\"data row4 col5\" >-0.20</td>\n",
              "      <td id=\"T_c2f8a_row4_col6\" class=\"data row4 col6\" >-0.28</td>\n",
              "      <td id=\"T_c2f8a_row4_col7\" class=\"data row4 col7\" >0.09</td>\n",
              "      <td id=\"T_c2f8a_row4_col8\" class=\"data row4 col8\" >0.04</td>\n",
              "      <td id=\"T_c2f8a_row4_col9\" class=\"data row4 col9\" >0.40</td>\n",
              "      <td id=\"T_c2f8a_row4_col10\" class=\"data row4 col10\" >-0.26</td>\n",
              "      <td id=\"T_c2f8a_row4_col11\" class=\"data row4 col11\" >-0.20</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th id=\"T_c2f8a_level0_row5\" class=\"row_heading level0 row5\" >free sulfur dioxide</th>\n",
              "      <td id=\"T_c2f8a_row5_col0\" class=\"data row5 col0\" >-0.28</td>\n",
              "      <td id=\"T_c2f8a_row5_col1\" class=\"data row5 col1\" >-0.35</td>\n",
              "      <td id=\"T_c2f8a_row5_col2\" class=\"data row5 col2\" >0.13</td>\n",
              "      <td id=\"T_c2f8a_row5_col3\" class=\"data row5 col3\" >0.40</td>\n",
              "      <td id=\"T_c2f8a_row5_col4\" class=\"data row5 col4\" >-0.20</td>\n",
              "      <td id=\"T_c2f8a_row5_col5\" class=\"data row5 col5\" >1.00</td>\n",
              "      <td id=\"T_c2f8a_row5_col6\" class=\"data row5 col6\" >0.72</td>\n",
              "      <td id=\"T_c2f8a_row5_col7\" class=\"data row5 col7\" >-0.01</td>\n",
              "      <td id=\"T_c2f8a_row5_col8\" class=\"data row5 col8\" >-0.15</td>\n",
              "      <td id=\"T_c2f8a_row5_col9\" class=\"data row5 col9\" >-0.19</td>\n",
              "      <td id=\"T_c2f8a_row5_col10\" class=\"data row5 col10\" >-0.18</td>\n",
              "      <td id=\"T_c2f8a_row5_col11\" class=\"data row5 col11\" >0.06</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th id=\"T_c2f8a_level0_row6\" class=\"row_heading level0 row6\" >total sulfur dioxide</th>\n",
              "      <td id=\"T_c2f8a_row6_col0\" class=\"data row6 col0\" >-0.33</td>\n",
              "      <td id=\"T_c2f8a_row6_col1\" class=\"data row6 col1\" >-0.41</td>\n",
              "      <td id=\"T_c2f8a_row6_col2\" class=\"data row6 col2\" >0.20</td>\n",
              "      <td id=\"T_c2f8a_row6_col3\" class=\"data row6 col3\" >0.50</td>\n",
              "      <td id=\"T_c2f8a_row6_col4\" class=\"data row6 col4\" >-0.28</td>\n",
              "      <td id=\"T_c2f8a_row6_col5\" class=\"data row6 col5\" >0.72</td>\n",
              "      <td id=\"T_c2f8a_row6_col6\" class=\"data row6 col6\" >1.00</td>\n",
              "      <td id=\"T_c2f8a_row6_col7\" class=\"data row6 col7\" >-0.00</td>\n",
              "      <td id=\"T_c2f8a_row6_col8\" class=\"data row6 col8\" >-0.24</td>\n",
              "      <td id=\"T_c2f8a_row6_col9\" class=\"data row6 col9\" >-0.28</td>\n",
              "      <td id=\"T_c2f8a_row6_col10\" class=\"data row6 col10\" >-0.27</td>\n",
              "      <td id=\"T_c2f8a_row6_col11\" class=\"data row6 col11\" >-0.04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th id=\"T_c2f8a_level0_row7\" class=\"row_heading level0 row7\" >density</th>\n",
              "      <td id=\"T_c2f8a_row7_col0\" class=\"data row7 col0\" >0.29</td>\n",
              "      <td id=\"T_c2f8a_row7_col1\" class=\"data row7 col1\" >0.06</td>\n",
              "      <td id=\"T_c2f8a_row7_col2\" class=\"data row7 col2\" >0.13</td>\n",
              "      <td id=\"T_c2f8a_row7_col3\" class=\"data row7 col3\" >0.18</td>\n",
              "      <td id=\"T_c2f8a_row7_col4\" class=\"data row7 col4\" >0.09</td>\n",
              "      <td id=\"T_c2f8a_row7_col5\" class=\"data row7 col5\" >-0.01</td>\n",
              "      <td id=\"T_c2f8a_row7_col6\" class=\"data row7 col6\" >-0.00</td>\n",
              "      <td id=\"T_c2f8a_row7_col7\" class=\"data row7 col7\" >1.00</td>\n",
              "      <td id=\"T_c2f8a_row7_col8\" class=\"data row7 col8\" >-0.02</td>\n",
              "      <td id=\"T_c2f8a_row7_col9\" class=\"data row7 col9\" >0.11</td>\n",
              "      <td id=\"T_c2f8a_row7_col10\" class=\"data row7 col10\" >-0.16</td>\n",
              "      <td id=\"T_c2f8a_row7_col11\" class=\"data row7 col11\" >-0.06</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th id=\"T_c2f8a_level0_row8\" class=\"row_heading level0 row8\" >pH</th>\n",
              "      <td id=\"T_c2f8a_row8_col0\" class=\"data row8 col0\" >-0.25</td>\n",
              "      <td id=\"T_c2f8a_row8_col1\" class=\"data row8 col1\" >0.26</td>\n",
              "      <td id=\"T_c2f8a_row8_col2\" class=\"data row8 col2\" >-0.33</td>\n",
              "      <td id=\"T_c2f8a_row8_col3\" class=\"data row8 col3\" >-0.27</td>\n",
              "      <td id=\"T_c2f8a_row8_col4\" class=\"data row8 col4\" >0.04</td>\n",
              "      <td id=\"T_c2f8a_row8_col5\" class=\"data row8 col5\" >-0.15</td>\n",
              "      <td id=\"T_c2f8a_row8_col6\" class=\"data row8 col6\" >-0.24</td>\n",
              "      <td id=\"T_c2f8a_row8_col7\" class=\"data row8 col7\" >-0.02</td>\n",
              "      <td id=\"T_c2f8a_row8_col8\" class=\"data row8 col8\" >1.00</td>\n",
              "      <td id=\"T_c2f8a_row8_col9\" class=\"data row8 col9\" >0.19</td>\n",
              "      <td id=\"T_c2f8a_row8_col10\" class=\"data row8 col10\" >0.12</td>\n",
              "      <td id=\"T_c2f8a_row8_col11\" class=\"data row8 col11\" >0.02</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th id=\"T_c2f8a_level0_row9\" class=\"row_heading level0 row9\" >sulphates</th>\n",
              "      <td id=\"T_c2f8a_row9_col0\" class=\"data row9 col0\" >0.30</td>\n",
              "      <td id=\"T_c2f8a_row9_col1\" class=\"data row9 col1\" >0.23</td>\n",
              "      <td id=\"T_c2f8a_row9_col2\" class=\"data row9 col2\" >0.06</td>\n",
              "      <td id=\"T_c2f8a_row9_col3\" class=\"data row9 col3\" >-0.19</td>\n",
              "      <td id=\"T_c2f8a_row9_col4\" class=\"data row9 col4\" >0.40</td>\n",
              "      <td id=\"T_c2f8a_row9_col5\" class=\"data row9 col5\" >-0.19</td>\n",
              "      <td id=\"T_c2f8a_row9_col6\" class=\"data row9 col6\" >-0.28</td>\n",
              "      <td id=\"T_c2f8a_row9_col7\" class=\"data row9 col7\" >0.11</td>\n",
              "      <td id=\"T_c2f8a_row9_col8\" class=\"data row9 col8\" >0.19</td>\n",
              "      <td id=\"T_c2f8a_row9_col9\" class=\"data row9 col9\" >1.00</td>\n",
              "      <td id=\"T_c2f8a_row9_col10\" class=\"data row9 col10\" >-0.00</td>\n",
              "      <td id=\"T_c2f8a_row9_col11\" class=\"data row9 col11\" >0.04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th id=\"T_c2f8a_level0_row10\" class=\"row_heading level0 row10\" >alcohol</th>\n",
              "      <td id=\"T_c2f8a_row10_col0\" class=\"data row10 col0\" >-0.10</td>\n",
              "      <td id=\"T_c2f8a_row10_col1\" class=\"data row10 col1\" >-0.04</td>\n",
              "      <td id=\"T_c2f8a_row10_col2\" class=\"data row10 col2\" >-0.01</td>\n",
              "      <td id=\"T_c2f8a_row10_col3\" class=\"data row10 col3\" >-0.36</td>\n",
              "      <td id=\"T_c2f8a_row10_col4\" class=\"data row10 col4\" >-0.26</td>\n",
              "      <td id=\"T_c2f8a_row10_col5\" class=\"data row10 col5\" >-0.18</td>\n",
              "      <td id=\"T_c2f8a_row10_col6\" class=\"data row10 col6\" >-0.27</td>\n",
              "      <td id=\"T_c2f8a_row10_col7\" class=\"data row10 col7\" >-0.16</td>\n",
              "      <td id=\"T_c2f8a_row10_col8\" class=\"data row10 col8\" >0.12</td>\n",
              "      <td id=\"T_c2f8a_row10_col9\" class=\"data row10 col9\" >-0.00</td>\n",
              "      <td id=\"T_c2f8a_row10_col10\" class=\"data row10 col10\" >1.00</td>\n",
              "      <td id=\"T_c2f8a_row10_col11\" class=\"data row10 col11\" >0.44</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th id=\"T_c2f8a_level0_row11\" class=\"row_heading level0 row11\" >quality</th>\n",
              "      <td id=\"T_c2f8a_row11_col0\" class=\"data row11 col0\" >-0.08</td>\n",
              "      <td id=\"T_c2f8a_row11_col1\" class=\"data row11 col1\" >-0.27</td>\n",
              "      <td id=\"T_c2f8a_row11_col2\" class=\"data row11 col2\" >0.09</td>\n",
              "      <td id=\"T_c2f8a_row11_col3\" class=\"data row11 col3\" >-0.04</td>\n",
              "      <td id=\"T_c2f8a_row11_col4\" class=\"data row11 col4\" >-0.20</td>\n",
              "      <td id=\"T_c2f8a_row11_col5\" class=\"data row11 col5\" >0.06</td>\n",
              "      <td id=\"T_c2f8a_row11_col6\" class=\"data row11 col6\" >-0.04</td>\n",
              "      <td id=\"T_c2f8a_row11_col7\" class=\"data row11 col7\" >-0.06</td>\n",
              "      <td id=\"T_c2f8a_row11_col8\" class=\"data row11 col8\" >0.02</td>\n",
              "      <td id=\"T_c2f8a_row11_col9\" class=\"data row11 col9\" >0.04</td>\n",
              "      <td id=\"T_c2f8a_row11_col10\" class=\"data row11 col10\" >0.44</td>\n",
              "      <td id=\"T_c2f8a_row11_col11\" class=\"data row11 col11\" >1.00</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ],
      "source": [
        "from matplotlib import colors\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "class MidpointNormalize(colors.Normalize):\n",
        "    \"\"\"\n",
        "    Normalise the colorbar so that diverging bars work there way either side from a prescribed midpoint value)\n",
        "    e.g. im=ax1.imshow(array, norm=MidpointNormalize(midpoint=0.,vmin=-100, vmax=100))\n",
        "    Code by Joe Kington\n",
        "    \"\"\"\n",
        "    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):\n",
        "        self.midpoint = midpoint\n",
        "        colors.Normalize.__init__(self, vmin, vmax, clip)\n",
        "\n",
        "    def __call__(self, value, clip=None):\n",
        "        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]\n",
        "        return np.ma.masked_array(np.interp(value, x, y), np.isnan(value))\n",
        "\n",
        "def background_gradient(s, cmap='bwr', low=0, high=0):\n",
        "    \"\"\"\n",
        "    Color correlations table according to specified colormap\n",
        "    \"\"\"\n",
        "    rng = s.max() - s.min()\n",
        "    norm = MidpointNormalize(s.min() - (rng * low), s.max() + (rng * high), 0)\n",
        "    normed = norm(s.values)\n",
        "    c = [colors.rgb2hex(x) for x in plt.colormaps.get_cmap(cmap)(normed)]\n",
        "    return ['background-color: %s' % color for color in c]\n",
        "\n",
        "df.drop(['color', 'class'], axis=1).corr().style.apply(background_gradient, axis=1).format(precision=2).set_properties(**{'color': 'black'})"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6w1LnHOwEOfL"
      },
      "source": [
        "## Лінійна регресія\n",
        "\n",
        "> Примітка: Залежність якості вина від інших розглянутих фіч є (скоріш за все) нелінійною. Тому точність моделі в цьому завданні буде невеликою.\n",
        "\n",
        "**Завдання 1**: Відокремте цільове значення `quality`, розділіть дані у співвідношенні 7:3 (30% - набір для тестування, використовуйте `random_state=42`) і попередньо обробіть дані за допомогою `StandardScaler`."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "DHWbM0DfEOfL"
      },
      "outputs": [],
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "\n",
        "reg_df = df.drop(['color', 'class'], axis=1)\n",
        "\n",
        "#Відокремлюємо цільове значення\n",
        "X=reg_df.drop(['quality'],axis=1)\n",
        "y=reg_df['quality']\n",
        "#Розділимо датасет на тренувальний і тестовий набір\n",
        "X_train, X_test, y_train, y_test = train_test_split (X, y, test_size=0.3, random_state=42)\n",
        "\n",
        "scaler = StandardScaler()\n",
        "X_train_scaled = scaler.fit_transform(X_train)\n",
        "X_test_scaled = scaler.transform(X_test)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NYgNOqwrEOfM"
      },
      "source": [
        "**Завдання 2**: Навчіть модель LASSO з $\\alpha = 0,01$ (слабка регулярізація) і масштабованими даними. Знову встановіть `random_state=42`"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "u8_3DFBnEOfM",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 656
        },
        "outputId": "784fe58d-b6fd-4748-cfff-bcb8aa84bc0d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Модель опрацювала 10 інформативних фіч\n",
            "Feature: 0, Score: 0.00713\n",
            "Feature: 1, Score: -0.21996\n",
            "Feature: 2, Score: -0.00000\n",
            "Feature: 3, Score: 0.08407\n",
            "Feature: 4, Score: -0.03130\n",
            "Feature: 5, Score: 0.06741\n",
            "Feature: 6, Score: -0.09364\n",
            "Feature: 7, Score: -0.00000\n",
            "Feature: 8, Score: 0.02110\n",
            "Feature: 9, Score: 0.07875\n",
            "Feature: 10, Score: 0.38105\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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AFOIFwAAYArxAgAATCFeAACAKcQLAAAwhXgBAACmEC8AAMAUV+Pl8OHDKisrU0pKiiZNmqQlS5bok08+GXL7O+64Q1//+tc1YcIETZ8+XXfeeadCoZCbYwIAAENcjZeysjK999572rZtm1588UW9/vrruv3220+4/YEDB3TgwAGtWbNG7777rn75y1+qqalJS5YscXNMAABgSJzjOI4bB961a5dmz56tnTt3qqCgQJLU1NSka6+9Vh9//LEyMzNP6TjPPfecbr75ZvX29iohIeGk24fDYfl8PoVCIaWkpJzW32BZdvVLsR5Be1eXxnoEAIARw3n+du3KS0tLiyZNmhQNF0ny+/3yeDzasWPHKR/n8z/iROHS19encDg8YAEAAOOXa/ESDAY1derUAesSEhKUmpqqYDB4Ssc4dOiQVq1aNeRLTYFAQD6fL7pkZWWd1twAAGBsG3a8VFdXKy4ubshl9+7dpz1YOBxWaWmpZs+erQcffPCE29XU1CgUCkWXzs7O0z43AAAYu05+E8n/c/fdd+vWW28dcpuZM2cqIyND3d3dA9Z/+umnOnz4sDIyMobcv6enRwsWLFBycrK2bt2qM84444Tber1eeb3eU54fAADYNux4mTJliqZMmXLS7YqLi3XkyBG1tbUpPz9fkvTKK68oEomoqKjohPuFw2GVlJTI6/XqhRdeUFJS0nBHBAAA45hr97zMmjVLCxYs0NKlS9Xa2qo333xTlZWVWrRoUfSdRvv371dOTo5aW1slfRYu11xzjXp7e/XUU08pHA4rGAwqGAyqv7/frVEBAIAhw77yMhzPPvusKisrNX/+fHk8Ht1www168skno78/fvy49uzZo6NHj0qS2tvbo+9EOv/88wcc66OPPlJ2drab4wIAAANcjZfU1FQ1Njae8PfZ2dn674+Zufrqq+XSx84AAIBxgu82AgAAphAvAADAFOIFAACYQrwAAABTXL1hF7HDlyICAMYrrrwAAABTiBcAAGAK8QIAAEwhXgAAgCnECwAAMIV4AQAAphAvAADAFOIFAACYQrwAAABTiBcAAGAK8QIAAEwhXgAAgCnECwAAMIV4AQAAphAvAADAlIRYDzDSHMeRJIXD4RhPAgAATtXnz9ufP48PZdzFS09PjyQpKysrxpMAAIDh6unpkc/nG3KbOOdUEseQSCSiAwcOKDk5WXFxcbEe50vC4bCysrLU2dmplJSUWI9jGo/lyOLxHDk8liOLx3PkjOXH0nEc9fT0KDMzUx7P0He1jLsrLx6PR+eee26sxziplJSUMfcfjlU8liOLx3Pk8FiOLB7PkTNWH8uTXXH5HDfsAgAAU4gXAABgCvEyyrxer2pra+X1emM9ink8liOLx3Pk8FiOLB7PkTNeHstxd8MuAAAY37jyAgAATCFeAACAKcQLAAAwhXgBAACmEC+jqL6+XtnZ2UpKSlJRUZFaW1tjPZJJgUBA8+bNU3JysqZOnarrr79ee/bsifVY48Lq1asVFxenFStWxHoUs/bv36+bb75ZZ599tiZMmKCLLrpIb7/9dqzHMqe/v18PPPCAZsyYoQkTJui8887TqlWrTul7byC9/vrruu6665SZmam4uDg9//zzA37vOI5Wrlypc845RxMmTJDf79ff//732Az7PyBeRsmWLVtUVVWl2tpatbe3Kzc3VyUlJeru7o71aOa89tprWrZsmd566y1t27ZNx48f1zXXXKPe3t5Yj2bazp079fOf/1wXX3xxrEcx69///rcuu+wynXHGGfrDH/6g999/X0888YQmT54c69HMefTRR7VhwwatX79eu3bt0qOPPqrHHntM69ati/VoJvT29io3N1f19fWD/v6xxx7Tk08+qYaGBu3YsUNnnXWWSkpK9J///GeUJ/0fORgVhYWFzrJly6I/9/f3O5mZmU4gEIjhVONDd3e3I8l57bXXYj2KWT09Pc4FF1zgbNu2zbnqqquc5cuXx3okk+69917n8ssvj/UY40Jpaalz2223DVj3ve99zykrK4vRRHZJcrZu3Rr9ORKJOBkZGc7jjz8eXXfkyBHH6/U6v/71r2Mw4fBx5WUUHDt2TG1tbfL7/dF1Ho9Hfr9fLS0tMZxsfAiFQpKk1NTUGE9i17Jly1RaWjrgv1EM3wsvvKCCggLdeOONmjp1qubOnatNmzbFeiyTLr30UjU3N+uDDz6QJP31r3/VG2+8oW9961sxnsy+jz76SMFgcMD/3n0+n4qKisw8J427L2Yciw4dOqT+/n6lp6cPWJ+enq7du3fHaKrxIRKJaMWKFbrssss0Z86cWI9j0ubNm9Xe3q6dO3fGehTz/vnPf2rDhg2qqqrSfffdp507d+rOO+9UYmKiysvLYz2eKdXV1QqHw8rJyVF8fLz6+/v18MMPq6ysLNajmRcMBiVp0Oekz3831hEvMG3ZsmV699139cYbb8R6FJM6Ozu1fPlybdu2TUlJSbEex7xIJKKCggI98sgjkqS5c+fq3XffVUNDA/EyTL/5zW/07LPPqrGxURdeeKE6Ojq0YsUKZWZm8liCG3ZHQ1pamuLj49XV1TVgfVdXlzIyMmI0lX2VlZV68cUX9eqrr+rcc8+N9TgmtbW1qbu7W5dccokSEhKUkJCg1157TU8++aQSEhLU398f6xFNOeecczR79uwB62bNmqV9+/bFaCK77rnnHlVXV2vRokW66KKLdMstt+iuu+5SIBCI9Wjmff68Y/k5iXgZBYmJicrPz1dzc3N0XSQSUXNzs4qLi2M4mU2O46iyslJbt27VK6+8ohkzZsR6JLPmz5+vd955Rx0dHdGloKBAZWVl6ujoUHx8fKxHNOWyyy770tv2P/jgA33ta1+L0UR2HT16VB7PwKeo+Ph4RSKRGE00fsyYMUMZGRkDnpPC4bB27Nhh5jmJl41GSVVVlcrLy1VQUKDCwkLV1dWpt7dXFRUVsR7NnGXLlqmxsVG/+93vlJycHH2N1ufzacKECTGezpbk5OQv3St01lln6eyzz+Yeov/BXXfdpUsvvVSPPPKIfvCDH6i1tVUbN27Uxo0bYz2aOdddd50efvhhTZ8+XRdeeKH+8pe/aO3atbrttttiPZoJn3zyiT788MPozx999JE6OjqUmpqq6dOna8WKFfrpT3+qCy64QDNmzNADDzygzMxMXX/99bEbejhi/Xanr5J169Y506dPdxITE53CwkLnrbfeivVIJkkadPnFL34R69HGBd4qfXp+//vfO3PmzHG8Xq+Tk5PjbNy4MdYjmRQOh53ly5c706dPd5KSkpyZM2c6999/v9PX1xfr0Ux49dVXB/3/yfLycsdxPnu79AMPPOCkp6c7Xq/XmT9/vrNnz57YDj0McY7DxxUCAAA7uOcFAACYQrwAAABTiBcAAGAK8QIAAEwhXgAAgCnECwAAMIV4AQAAphAvAADAFOIFAACYQrwAAABTiBcAAGAK8QIAAEz5PyXpqUEKRPiBAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "За графіком найменш інформативна фіча це 2 тобіж - citric acid\n"
          ]
        }
      ],
      "source": [
        "from matplotlib import pyplot\n",
        "from sklearn.linear_model import Lasso\n",
        "\n",
        "lasso = Lasso(alpha=0.01, random_state=42)\n",
        "#Навчаємо модель на створених даних\n",
        "lasso.fit(X_train_scaled, y_train)\n",
        "\n",
        "count = 1\n",
        "for i in lasso.coef_:\n",
        "    if i != 0:\n",
        "        count += 1\n",
        "\n",
        "\n",
        "print(f'Модель опрацювала {count} інформативних фіч')\n",
        "#Відсортуйте фічі за їх впливом на цільове значення (якість вина).\n",
        "importance = lasso.coef_\n",
        "for i,v in enumerate(importance):\n",
        " print('Feature: %0d, Score: %.5f' % (i,v))\n",
        "\n",
        "pyplot.bar([x for x in range(len(importance))], importance)\n",
        "pyplot.show()\n",
        "\n",
        "print(f'За графіком найменш інформативна фіча це 2 тобіж - citric acid')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dplgavkIEOfN"
      },
      "source": [
        "Відсортуйте фічі за їх впливом на цільове значення (якість вина). Майте на увазі, що як великі позитивні, так і великі негативні коефіцієнти означають великий вплив на цільове значення. Тут зручно використовувати `pandas.DataFrame`.\n",
        "\n",
        "**Завдання 3**: Яка фіча є найменш інформативною для прогнозування якості вина, згідно з цією моделлю LASSO?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "oOAxbDfhEOfN",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3094235b-70c8-45be-c6e1-30bf1407967a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Найменш інформативна фіча: citric acid\n"
          ]
        }
      ],
      "source": [
        "lasso_coef = pd.DataFrame({'Feature': X.columns, 'Importance': lasso.coef_})\n",
        "lasso_coef_sorted = lasso_coef.sort_values(by='Importance', key=lambda x: x.abs())\n",
        "\n",
        "least_Importance_feature = lasso_coef_sorted.iloc[0]['Feature']\n",
        "\n",
        "print(f\"Найменш інформативна фіча: {least_Importance_feature}\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "99PI2J_WEOfN"
      },
      "source": [
        "**Завдання 4**: Навчіть `LassoCV` із `random_state=42`, щоб вибрати найкраще значення $\\alpha$ у 5-кратній перехресній перевірці. Скористайтесь масштабованими даними."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "deUQaCXdEOfO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2a086f19-7bed-4ba1-d64c-c993c33e7bb9"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.0009437878277775381"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ],
      "source": [
        "from sklearn.linear_model import LassoCV\n",
        "\n",
        "alphas = np.logspace(-6, 2, 200)\n",
        "lasso_cv = LassoCV(random_state=42, cv=5, alphas=alphas)\n",
        "lasso_cv.fit(X_train_scaled, y_train)\n",
        "lasso_cv.alpha_"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "h1q8AkPMEOfO"
      },
      "source": [
        "**Завдання 5**: Яка фіча є найменш інформативною для прогнозування якості вина, згідно налаштованої моделі LASSO?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "lyEnQj93EOfO",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 411
        },
        "outputId": "342da6e9-8265-4e48-b77e-8fcbc65bfc38"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Найменш інформативна фіча для налаштованої моделі): 0.00892923206547775\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "        coef  coef_abs\n",
              "7  -0.008929  0.008929\n",
              "2  -0.017402  0.017402\n",
              "0   0.034102  0.034102\n",
              "8   0.037194  0.037194\n",
              "4  -0.040485  0.040485\n",
              "9   0.088221  0.088221\n",
              "5   0.095857  0.095857\n",
              "3   0.108698  0.108698\n",
              "6  -0.125872  0.125872\n",
              "1  -0.242293  0.242293\n",
              "10  0.391589  0.391589"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-ef619cca-87b6-4936-bea4-d809e9ab91f5\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>coef</th>\n",
              "      <th>coef_abs</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>-0.008929</td>\n",
              "      <td>0.008929</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>-0.017402</td>\n",
              "      <td>0.017402</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0.034102</td>\n",
              "      <td>0.034102</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>0.037194</td>\n",
              "      <td>0.037194</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>-0.040485</td>\n",
              "      <td>0.040485</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>0.088221</td>\n",
              "      <td>0.088221</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>0.095857</td>\n",
              "      <td>0.095857</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0.108698</td>\n",
              "      <td>0.108698</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>-0.125872</td>\n",
              "      <td>0.125872</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>-0.242293</td>\n",
              "      <td>0.242293</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>0.391589</td>\n",
              "      <td>0.391589</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-ef619cca-87b6-4936-bea4-d809e9ab91f5')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-ef619cca-87b6-4936-bea4-d809e9ab91f5 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-ef619cca-87b6-4936-bea4-d809e9ab91f5');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-191489e1-3ff1-41ae-a761-372c7cc3e476\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-191489e1-3ff1-41ae-a761-372c7cc3e476')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-191489e1-3ff1-41ae-a761-372c7cc3e476 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ],
      "source": [
        "lasso_cv_coef = pd.DataFrame({\"coef\": lasso_cv.coef_, \"coef_abs\": np.abs(lasso_cv.coef_)})\n",
        "lasso_cv_coef_sorted = lasso_cv_coef.sort_values(by=\"coef_abs\")\n",
        "\n",
        "least_importance_feature_cv = lasso_cv_coef_sorted.iloc[0]['coef_abs']\n",
        "print(f\"Найменш інформативна фіча для налаштованої моделі): {least_importance_feature_cv}\")  #density\n",
        "\n",
        "lasso_cv_coef.sort_values(by=\"coef_abs\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tPYYU72AEOfO"
      },
      "source": [
        "**Завдання 6**: Які середнь- квадратичні помилки прогнозування налаштованої моделі LASSO на тренувальному і тестовому наборах даних? Скористайтесь масштабованими даними."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "FVjDpkcHEOfP"
      },
      "outputs": [],
      "source": [
        "from sklearn.metrics import mean_squared_error\n",
        "Mean_squared_error1 = mean_squared_error(y_train, lasso_cv.predict(X_train_scaled))\n",
        "Mean_squared_error2 = mean_squared_error(y_test, lasso_cv.predict(X_test_scaled))\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "yLnIxVjPEOfP"
      },
      "source": [
        "## Класифікація\n",
        "\n",
        "**Завдання 7**: Відокремте цільове значення `class`, розділіть дані у співвідношенні 7:3 (30% - набір для тестування, використовуйте `random_state=42`) і попередньо обробіть дані за допомогою `StandardScaler`."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "zlm141BREOfP"
      },
      "outputs": [],
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "\n",
        "tree_df = df.drop(['color', 'quality'], axis=1)\n",
        "\n",
        "\n",
        "#Відокремлюємо цільове значення\n",
        "X=tree_df.drop(['class'],axis=1)\n",
        "y=tree_df['class']\n",
        "#Розділимо датасет на тренувальний і тестовий набір\n",
        "X_train, X_test, y_train, y_test = train_test_split (X, y, test_size=0.3, random_state=42)\n",
        "\n",
        "scaler = StandardScaler()\n",
        "X_train_scaled = scaler.fit_transform(X_train)\n",
        "X_test_scaled = scaler.transform(X_test)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XrM9pb6TEOfQ"
      },
      "source": [
        "**Завдання 8**: Навчіть дерево рішень (`random_state=42`). Знайдіть оптимальну максимальну глибину за допомогою 5-кратної перехресної перевірки (`GridSearchCV`). Скористайтесь масштабованими даними."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "C8sCkyXLEOfQ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "44af693d-4d1f-4ce2-a906-91591f89e230"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Best params: {'max_depth': 6}\n",
            "Best cross validaton score 0.8299955270252299\n"
          ]
        }
      ],
      "source": [
        "from sklearn.model_selection import GridSearchCV\n",
        "from sklearn.tree import DecisionTreeClassifier\n",
        "\n",
        "tree_params = {\"max_depth\": range(2, 11)}\n",
        "\n",
        "best_tree = GridSearchCV(DecisionTreeClassifier(random_state=42), tree_params, cv=5)\n",
        "\n",
        "best_tree.fit(X_train_scaled, y_train)\n",
        "print(\"Best params:\", best_tree.best_params_)\n",
        "print(\"Best cross validaton score\", best_tree.best_score_)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "J0gd_qreEOfQ"
      },
      "source": [
        "**Завдання 9**: Навчіть дерево рішень із кращою максимальною глибиною `max_depth` яку ви отримаєте у попередньому кроці і обчисліть точність на тестовому набору. Використовуйте параметр `random_state = 42` для відтворюваності. Скористайтесь масштабованими даними."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "nvZ24QnCEOfQ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "09081766-0c3a-4776-a3db-3957a9347c75"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Точність: 0.8292307692307692\n"
          ]
        }
      ],
      "source": [
        "# В попередньому блоці коду я отримав  {'max_depth': 9}\n",
        "from sklearn.metrics import accuracy_score\n",
        "\n",
        "tuned_tree = DecisionTreeClassifier(max_depth=9, random_state=42)\n",
        "tuned_tree.fit(X_train, y_train)\n",
        "tuned_tree_predictions = tuned_tree.predict(X_test)\n",
        "accuracy_score(y_test, tuned_tree_predictions)\n",
        "print(\"Точність:\", accuracy_score(y_test, tuned_tree_predictions))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OFLMq__OEOfR"
      },
      "source": [
        "## Зменшення розмірності\n",
        "\n",
        "Ми знаємо що дані у нас достатньо корельовані, тому ми можемо зменшити кількість фіч при цьому зберігаючи достатню різноманітність даних.\n",
        "\n",
        "**Завдання 10**: Відокремте цільове значення `class` і попередньо обробіть дані за допомогою `StandardScaler`. Розділяти дані немає необхідності, оскільки ми в подальшому будемо використовувати кластеризацію."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "pDz1zr1WEOfS"
      },
      "outputs": [],
      "source": [
        "from sklearn.preprocessing import StandardScaler\n",
        "\n",
        "cluster_df = df.drop(['color', 'quality'], axis=1)\n",
        "X = cluster_df.drop('class', axis=1)\n",
        "y = cluster_df['class']\n",
        "\n",
        "scaler = StandardScaler()\n",
        "X_scaled = scaler.fit_transform(X)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "P1cq6bulEOfS"
      },
      "source": [
        "**Завдання 11**: Зменшіть кількість вимірів за допомогою PCA, залишивши стільки компонентів, скільки необхідно для пояснення принаймні 90% дисперсії вихідних (масштабованих) даних. Використовуйте масштабований набір даних і `random_state=42`."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "j78oSc5eEOfS"
      },
      "outputs": [],
      "source": [
        "from sklearn.decomposition import PCA\n",
        "\n",
        "pca = PCA(n_components=0.9, random_state=42).fit(X_scaled)\n",
        "X_pca = pca.transform(X_scaled)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UpdLdeFLEOfT"
      },
      "source": [
        "**Завдання 12**: Яка мінімальна кількість головних компонентів потрібна для покриття 90% дисперсії вихідних (масштабованих) даних?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "WYHbZ6LFEOfT",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "cac048f6-19f8-4f5e-ecec-b0da4f84cbd7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Мінімальна кількість головних компонент для покриття 90% дисперсії: {0.9}\n"
          ]
        }
      ],
      "source": [
        "print('Мінімальна кількість головних компонент для покриття 90% дисперсії:',{pca.fit(X_scaled).n_components})"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VLq1xU16EOfi"
      },
      "source": [
        "**Завдання 13**: Який відсоток дисперсії покриває перший головний компонент? Округліть до найближчого відсотка."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "58zV6SfUEOfi",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "af540a19-0770-47e4-fc1d-e501d81218e4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "відсоток дисперсії покриває перший головний компонент \t 28 %\n"
          ]
        }
      ],
      "source": [
        "print('відсоток дисперсії покриває перший головний компонент \\t',round(float(pca.explained_variance_ratio_[0] * 100)),'%')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Jvr7APJ5EOfi"
      },
      "source": [
        "**Завдання 14**: Візуалізуйте дані в проекції на перші два основні компоненти. Використайте `Seaborn`."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "2A7N18dPEOfi",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 449
        },
        "outputId": "d9136c40-9ac7-48ca-a88a-cb1dc90b4d02"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "pca = PCA(n_components=2, random_state=42)\n",
        "pca_2 = pca.fit_transform(X_scaled)\n",
        "pca_df = pd.DataFrame(data=pca_2, columns=['Class1', 'Class2'])\n",
        "\n",
        "pca_df['Class'] = y.values\n",
        "\n",
        "sns.scatterplot(x='Class1', y='Class2', hue='Class', data=pca_df)\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3G-gF9hOEOfj"
      },
      "source": [
        "Ви побачите якусь кількість кластерів, але можливо побачене вас не втішить :)\n",
        "\n",
        "## Кластеризація\n",
        "**Завдання 14**: Виконайте кластеризацію за допомогою методу `KMeans`, навчаючи модель на даних зі зменшеною розмірністю (за допомогою PCA). У цьому випадку ми шукаємо рівно 2 кластери (оскільки ми знаємо що у нас два класи), але в загальному випадку ми не будемо знати, скільки кластерів нам слід шукати.\n",
        "\n",
        "Опції:\n",
        "- `n_clusters` = 2 (кількість унікальних міток цільового класу)\n",
        "- `n_init` = 100\n",
        "- `random_state` = 42 (для відтворюваності результату)\n",
        "\n",
        "Інші параметри повинні мати значення за замовчуванням."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "X6y8RbjtEOfj"
      },
      "outputs": [],
      "source": [
        "from sklearn.cluster import KMeans\n",
        "\n",
        "kmeans = KMeans(n_clusters=2, n_init=100, random_state=42)\n",
        "kmeans.fit(X_pca)\n",
        "cluster_labels = kmeans.labels_"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "40HtywD2EOfj"
      },
      "source": [
        "**Завдання 15**: Візуалізуйте дані в проекції на перші два основні компоненти. Розфарбуйте точки відповідно до отриманих кластерів."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "0Q24qynpEOfj",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 430
        },
        "outputId": "a0c4528e-72dc-47d4-9643-327b7b8e0a6e"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "plt.scatter(X_pca[:, 0], X_pca[:, 1], c=cluster_labels, s=20, cmap=\"Set2\");\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SXZ79H_AEOfj"
      },
      "source": [
        "Подивіться на відповідність між позначками кластера та початковими мітками класу, а також на те, як їх плутає `KMeans` :)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "9P1ioaOwEOfk",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 143
        },
        "outputId": "0d653b68-06ee-4ae7-8d5c-19bd3d4c4839"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "      cluster1  cluster2   all\n",
              "high      1055       222  1277\n",
              "low       3756      1464  5220\n",
              "all       4811      1686  6497"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-4a7d1741-0dcc-43b6-a03b-7a21bc57ce1d\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>cluster1</th>\n",
              "      <th>cluster2</th>\n",
              "      <th>all</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>high</th>\n",
              "      <td>1055</td>\n",
              "      <td>222</td>\n",
              "      <td>1277</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>low</th>\n",
              "      <td>3756</td>\n",
              "      <td>1464</td>\n",
              "      <td>5220</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>all</th>\n",
              "      <td>4811</td>\n",
              "      <td>1686</td>\n",
              "      <td>6497</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-4a7d1741-0dcc-43b6-a03b-7a21bc57ce1d')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-4a7d1741-0dcc-43b6-a03b-7a21bc57ce1d button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-4a7d1741-0dcc-43b6-a03b-7a21bc57ce1d');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-5a5a6571-5960-4d1c-90e3-afd7333002ef\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-5a5a6571-5960-4d1c-90e3-afd7333002ef')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-5a5a6571-5960-4d1c-90e3-afd7333002ef button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 90
        }
      ],
      "source": [
        "tab = pd.crosstab(y, cluster_labels, margins=True)\n",
        "tab.index = [\n",
        "     \"high\",\n",
        "     \"low\",\n",
        "     \"all\",\n",
        "]\n",
        "tab.columns = [\"cluster\" + str(i + 1) for i in range(2)] + [\"all\"]\n",
        "tab\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3xEYGrWqEOfk"
      },
      "source": [
        "Ми бачимо, що для кожного класу є кілька кластерів. Давайте розглянемо максимальний відсоток об’єктів у класі, які віднесли до одного кластеру. Це буде проста метрика, яка характеризує, наскільки легко клас відокремлюється від інших під час кластеризації.\n",
        "\n",
        "Приклад: якщо для класу «high» (з 1277 екземплярами, що належать до нього), розподіл кластерів є:\n",
        "  - кластер 1 - 1062\n",
        "  - кластер 3 - 215\n",
        "\n",
        "то така частка буде 1062/1277 $ \\approx $ 0,83.\n",
        "\n",
        "**Завдання 16**: Який клас відокремлений краще на основі простого показника, описаного вище?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "HLYQoS7JEOfk",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "92db8ebc-2e50-4d5f-a1e5-31a811bb24d2"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "high    0.826155\n",
              "low     0.719540\n",
              "dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 94
        }
      ],
      "source": [
        "pd.Series(tab.iloc[:-1, :-1].max(axis=1).values / tab.iloc[:-1, -1].values,index=tab.index[:-1])\n",
        "#high клас відокремлений краще"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "v-z2n7wzEOfk"
      },
      "source": [
        "Можна побачити, що kMeans не дуже добре розрізняє класи. Давайте дізнаємось чи PCA допоможе класифікації (оскільки ми знаємо класи).\n",
        "\n",
        "**Завдання 17**: Навчіть дерево рішень (`random_state=42`). Знайдіть оптимальну максимальну глибину за допомогою 5-кратної перехресної перевірки (`GridSearchCV`). Скористайтесь даними зі зменшеною розмірністю (за допомогою PCA)."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "XfuZYCDdEOfl",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d95e6561-476d-49c9-82bc-4e15489d1c38"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Best params: {'max_depth': 10}\n",
            "Best cross validaton score 0.8320729555279209\n"
          ]
        }
      ],
      "source": [
        "from sklearn.model_selection import GridSearchCV\n",
        "from sklearn.tree import DecisionTreeClassifier\n",
        "\n",
        "tree_params = {\"max_depth\": range(2, 11)}\n",
        "best_tree = GridSearchCV(DecisionTreeClassifier(random_state=42),tree_params, cv=5)\n",
        "\n",
        "#best_tree.fit(X_train, y_train)\n",
        "#best_tree.fit(X_train, y)\n",
        "best_tree.fit(X_pca, y)\n",
        "print(\"Best params:\", best_tree.best_params_)\n",
        "print(\"Best cross validaton score\", best_tree.best_score_)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wi585FzbEOfl"
      },
      "source": [
        "Загалом, ситуація не покращилась (або стало гірше). Але (сподіваюсь) стало зрозуміло, що конкретні алгоритми машинного навчання не можна застосувати для рішення всіх задач, і вихідний набір даних впливає їх ефективність.\n",
        "\n",
        "Тому, дуже часто треба або перебирати різні алгоритми в пошуках того, який краще вирішить задачу або використовувати методи фіча інжинірінгу для допомоги (про що ми поговоримо на наступних лекціях)."
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "venv",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.11.6"
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}