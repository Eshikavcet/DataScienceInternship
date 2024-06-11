{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "BePPhbnM_5iH",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "4523a239-a38d-4cbf-c486-ececbb395e8b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello world\n"
          ]
        }
      ],
      "source": [
        "print(\"Hello world\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=5\n",
        "m=6\n",
        "y=\"9\"\n",
        "z=\"5\"\n",
        "print(type(x))\n",
        "print(type(y))\n",
        "print(x+m)\n",
        "print(y+z)\n",
        "print(len(y))\n",
        "print(z[0])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7awkgl-WBAtC",
        "outputId": "0c2a9116-b61f-4723-d580-180953fb0064"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'int'>\n",
            "<class 'str'>\n",
            "11\n",
            "95\n",
            "1\n",
            "5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#typecasting\n",
        "a=int(z)\n",
        "print(a+m)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "n5jNwx8vBbnJ",
        "outputId": "ef4988ce-e3e0-414d-b0bc-9907d6349b97"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "11\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#list\n",
        "l1=['hi',1,7,\"list\",6.7,9.5,[3,89,\"hello\"]]\n",
        "l2=l1[6][2]\n",
        "print(l2)\n",
        "length=len(l1)\n",
        "print(length)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qPHtn_vjCKvK",
        "outputId": "822e6e8e-4f3e-4a8e-b270-640ba1ac8271"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello\n",
            "7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "nums=[]\n",
        "nums.append(21)\n",
        "nums.append(40.5)\n",
        "nums.append(\"String\")\n",
        "print(nums)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3mBy0OkyFCNv",
        "outputId": "eb30f03f-3e8f-4236-e4ce-2cd2e421d595"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[21, 40.5, 'String']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#tuple\n",
        "t1=(1,2,3,4,5,6,7,8)\n",
        "print(t1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AG-tYSliFoSf",
        "outputId": "fc0b8a1a-8939-4c75-ca85-5d3721f636ca"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(1, 2, 3, 4, 5, 6, 7, 8)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#dictionary\n",
        "d1={\"Name\":\"Esh\",\"Age\":\"18\",\"Proff\":\"Student\"}\n",
        "print(d1)\n",
        "print(type(d1))\n",
        "print(d1.keys())\n",
        "print(d1.values())\n",
        "print(d1.items())\n",
        "print(d1[\"Name\"])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rotk5-SfFxpO",
        "outputId": "5bda4909-d569-4d7e-e0af-5991ed6152ca"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'Name': 'Esh', 'Age': '18', 'Proff': 'Student'}\n",
            "<class 'dict'>\n",
            "dict_keys(['Name', 'Age', 'Proff'])\n",
            "dict_values(['Esh', '18', 'Student'])\n",
            "dict_items([('Name', 'Esh'), ('Age', '18'), ('Proff', 'Student')])\n",
            "Esh\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num1=int(input(\"Enter num1\"))\n",
        "num2=int(input(\"Enter num2\"))\n",
        "num3=num1+num2\n",
        "print(\"Product:\",num3)\n",
        "\n",
        "num1=int(input(\"Enter a number:\"))\n",
        "if num1>12:\n",
        "  print(\"Number is greater than 12\")\n",
        "else:\n",
        "  print(\"Number is smaller than 12\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 356
        },
        "id": "Dvx376wzHlWP",
        "outputId": "3b888d1d-9ce7-4b6b-a76a-f73c8cbc6fe9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "Interrupted by user",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-24-70f40d17e8f6>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mnum1\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Enter num1\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mnum2\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Enter num2\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mnum3\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mnum1\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0mnum2\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Product:\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mnum3\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m    849\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    850\u001b[0m             )\n\u001b[0;32m--> 851\u001b[0;31m         return self._input_request(str(prompt),\n\u001b[0m\u001b[1;32m    852\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    853\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m    893\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    894\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 895\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    896\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    897\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ]
    }
  ]
}