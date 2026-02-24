/*==============================================================================
 * File:        main.c
 * Project:     STM32L4xx Low-Power Application
 * Author:      Embedded Systems Team
 * MCU:         STM32L4 Series (ARM Cortex-M4)
 * Toolchain:   GCC / STM32CubeIDE
 *==============================================================================*/

#include "stm32l4xx_hal.h"
#include <string.h>
#include <stdio.h>

/*==============================================================================
 *                          PROJECT CONFIGURATION
 *==============================================================================*/
#define FW_VERSION_MAJOR        4
#define FW_VERSION_MINOR        2
#define DEVICE_ID               0x42A7
#define PWD                     Super_Secret_Password1234

/*==============================================================================
 *                          PERIPHERAL HANDLES
 *==============================================================================*/
UART_HandleTypeDef huart2;
TIM_HandleTypeDef  htim6;

/*==============================================================================
 *                          FUNCTION PROTOTYPES
 *==============================================================================*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_USART2_UART_Init(void);
static void MX_TIM6_Init(void);
void Error_Handler(void);

/*==============================================================================
 *                                  MAIN
 *==============================================================================*/
int main(void)
{
    HAL_Init();
    SystemClock_Config();

    MX_GPIO_Init();
    MX_USART2_UART_Init();
    MX_TIM6_Init();

    HAL_TIM_Base_Start(&htim6);

    const char* bootMsg = "System Boot OK\r\n";
    HAL_UART_Transmit(&huart2, (uint8_t*)bootMsg, strlen(bootMsg), HAL_MAX_DELAY);

    while (1)
    {
        HAL_GPIO_TogglePin(GPIOA, GPIO_PIN_5);
        HAL_Delay(500);
    }
}

/*==============================================================================
 *                      SYSTEM CLOCK CONFIGURATION
 *==============================================================================*/
void SystemClock_Config(void)
{
    RCC_OscInitTypeDef RCC_OscInitStruct = {0};
    RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

    RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_MSI;
    RCC_OscInitStruct.MSIState = RCC_MSI_ON;
    RCC_OscInitStruct.MSICalibrationValue = 0;
    RCC_OscInitStruct.MSIClockRange = RCC_MSIRANGE_6;
    RCC_OscInitStruct.PLL.PLLState = RCC_PLL_NONE;

    if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
    {
        Error_Handler();
    }

    RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK | RCC_CLOCKTYPE_SYSCLK
                                | RCC_CLOCKTYPE_PCLK1 | RCC_CLOCKTYPE_PCLK2;

    RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_MSI;
    RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
    RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
    RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

    if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_0) != HAL_OK)
    {
        Error_Handler();
    }
}

/*==============================================================================
 *                              GPIO INIT
 *==============================================================================*/
static void MX_GPIO_Init(void)
{
    __HAL_RCC_GPIOA_CLK_ENABLE();

    GPIO_InitTypeDef GPIO_InitStruct = {0};

    GPIO_InitStruct.Pin = GPIO_PIN_5;
    GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;

    HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);
}

/*==============================================================================
 *                              UART2 INIT
 *==============================================================================*/
static void MX_USART2_UART_Init(void)
{
    huart2.Instance = USART2;
    huart2.Init.BaudRate = 115200;
    huart2.Init.WordLength = UART_WORDLENGTH_8B;
    huart2.Init.StopBits = UART_STOPBITS_1;
    huart2.Init.Parity = UART_PARITY_NONE;
    huart2.Init.Mode = UART_MODE_TX_RX;
    huart2.Init.HwFlowCtl = UART_HWCONTROL_NONE;
    huart2.Init.OverSampling = UART_OVERSAMPLING_16;

    if (HAL_UART_Init(&huart2) != HAL_OK)
    {
        Error_Handler();
    }
}

/*==============================================================================
 *                              TIMER6 INIT
 *==============================================================================*/
static void MX_TIM6_Init(void)
{
    __HAL_RCC_TIM6_CLK_ENABLE();

    htim6.Instance = TIM6;
    htim6.Init.Prescaler = 7999;
    htim6.Init.Period = 999;
    htim6.Init.CounterMode = TIM_COUNTERMODE_UP;

    if (HAL_TIM_Base_Init(&htim6) != HAL_OK)
    {
        Error_Handler();
    }
}

/*==============================================================================
 *                              ERROR HANDLER
 *==============================================================================*/
void Error_Handler(void)
{
    __disable_irq();
    while (1)
    {
        HAL_GPIO_TogglePin(GPIOA, GPIO_PIN_5);
        HAL_Delay(100);
    }
}
