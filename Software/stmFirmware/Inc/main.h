/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2020 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under Ultimate Liberty license
  * SLA0044, the "License"; You may not use this file except in compliance with
  * the License. You may obtain a copy of the License at:
  *                             www.st.com/SLA0044
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32l4xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define SW0_Pin GPIO_PIN_0
#define SW0_GPIO_Port GPIOA
#define SW1_Pin GPIO_PIN_1
#define SW1_GPIO_Port GPIOA
#define SW2_Pin GPIO_PIN_2
#define SW2_GPIO_Port GPIOA
#define SW3_Pin GPIO_PIN_3
#define SW3_GPIO_Port GPIOA
#define SW4_Pin GPIO_PIN_4
#define SW4_GPIO_Port GPIOA
#define SW5_Pin GPIO_PIN_5
#define SW5_GPIO_Port GPIOA
#define SW6_Pin GPIO_PIN_6
#define SW6_GPIO_Port GPIOA
#define SW7_Pin GPIO_PIN_7
#define SW7_GPIO_Port GPIOA
#define SW8_Pin GPIO_PIN_8
#define SW8_GPIO_Port GPIOA
#define SW9_Pin GPIO_PIN_9
#define SW9_GPIO_Port GPIOA
#define SW10_Pin GPIO_PIN_10
#define SW10_GPIO_Port GPIOA
#define SW11_Pin GPIO_PIN_15
#define SW11_GPIO_Port GPIOA
/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
