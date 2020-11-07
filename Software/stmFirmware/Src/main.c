/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
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
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "usb_device.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include "usbd_cdc_if.h"
#include <stdbool.h>
/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */
bool btn_flank_flags[12] = {false};	
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
/* USER CODE BEGIN PFP */
void update_btn_flank_flags(void);
void vcp_send_switch(uint8_t switchNr);
/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_USB_DEVICE_Init();
  /* USER CODE BEGIN 2 */

  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  { 
		if(HAL_GPIO_ReadPin(SW0_GPIO_Port,SW0_Pin) && !btn_flank_flags[0])
			vcp_send_switch(0);
		if(HAL_GPIO_ReadPin(SW1_GPIO_Port,SW1_Pin) && !btn_flank_flags[1])
			vcp_send_switch(1);
		if(HAL_GPIO_ReadPin(SW2_GPIO_Port,SW2_Pin) && !btn_flank_flags[2])
			vcp_send_switch(2);
		if(HAL_GPIO_ReadPin(SW3_GPIO_Port,SW3_Pin) && !btn_flank_flags[3])
			vcp_send_switch(3);
		if(HAL_GPIO_ReadPin(SW4_GPIO_Port,SW4_Pin) && !btn_flank_flags[4])
			vcp_send_switch(4);
		if(HAL_GPIO_ReadPin(SW5_GPIO_Port,SW5_Pin) && !btn_flank_flags[5])
			vcp_send_switch(5);
		if(HAL_GPIO_ReadPin(SW6_GPIO_Port,SW6_Pin) && !btn_flank_flags[6])
			vcp_send_switch(6);
		if(HAL_GPIO_ReadPin(SW7_GPIO_Port,SW7_Pin) && !btn_flank_flags[7])
			vcp_send_switch(7);
		if(HAL_GPIO_ReadPin(SW8_GPIO_Port,SW8_Pin) && !btn_flank_flags[8])
			vcp_send_switch(8);
		if(HAL_GPIO_ReadPin(SW9_GPIO_Port,SW9_Pin) && !btn_flank_flags[9])
			vcp_send_switch(9);
		if(HAL_GPIO_ReadPin(SW10_GPIO_Port,SW10_Pin) && !btn_flank_flags[10])
			vcp_send_switch(10);
		if(HAL_GPIO_ReadPin(SW11_GPIO_Port,SW11_Pin) && !btn_flank_flags[11])
			vcp_send_switch(11);
		
		update_btn_flank_flags();
		
		HAL_Delay(10); // wait 10ms
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};
  RCC_PeriphCLKInitTypeDef PeriphClkInit = {0};

  /** Configure the main internal regulator output voltage
  */
  if (HAL_PWREx_ControlVoltageScaling(PWR_REGULATOR_VOLTAGE_SCALE1) != HAL_OK)
  {
    Error_Handler();
  }
  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_LSE|RCC_OSCILLATORTYPE_MSI;
  RCC_OscInitStruct.LSEState = RCC_LSE_BYPASS;
  RCC_OscInitStruct.MSIState = RCC_MSI_ON;
  RCC_OscInitStruct.MSICalibrationValue = 0;
  RCC_OscInitStruct.MSIClockRange = RCC_MSIRANGE_11;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_NONE;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }
  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_MSI;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
  {
    Error_Handler();
  }
  PeriphClkInit.PeriphClockSelection = RCC_PERIPHCLK_USB;
  PeriphClkInit.UsbClockSelection = RCC_USBCLKSOURCE_MSI;
  if (HAL_RCCEx_PeriphCLKConfig(&PeriphClkInit) != HAL_OK)
  {
    Error_Handler();
  }
  /** Enable MSI Auto calibration
  */
  HAL_RCCEx_EnableMSIPLLMode();
}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();

  /*Configure GPIO pins : SW2_Pin SW3_Pin SW7_Pin SW6_Pin
                           SW11_Pin SW10_Pin SW9_Pin SW8_Pin
                           SW5_Pin SW4_Pin SW0_Pin SW1_Pin */
  GPIO_InitStruct.Pin = SW2_Pin|SW3_Pin|SW7_Pin|SW6_Pin
                          |SW11_Pin|SW10_Pin|SW9_Pin|SW8_Pin
                          |SW5_Pin|SW4_Pin|SW0_Pin|SW1_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

}

/* USER CODE BEGIN 4 */
void update_btn_flank_flags(void)
{
	btn_flank_flags[0] = HAL_GPIO_ReadPin(SW0_GPIO_Port,SW0_Pin);
	btn_flank_flags[1] = HAL_GPIO_ReadPin(SW1_GPIO_Port,SW1_Pin);
	btn_flank_flags[2] = HAL_GPIO_ReadPin(SW2_GPIO_Port,SW2_Pin);
	btn_flank_flags[3] = HAL_GPIO_ReadPin(SW3_GPIO_Port,SW3_Pin);
	btn_flank_flags[4] = HAL_GPIO_ReadPin(SW4_GPIO_Port,SW4_Pin);
	btn_flank_flags[5] = HAL_GPIO_ReadPin(SW5_GPIO_Port,SW5_Pin);
	btn_flank_flags[6] = HAL_GPIO_ReadPin(SW6_GPIO_Port,SW6_Pin);
	btn_flank_flags[7] = HAL_GPIO_ReadPin(SW7_GPIO_Port,SW7_Pin);
	btn_flank_flags[8] = HAL_GPIO_ReadPin(SW8_GPIO_Port,SW8_Pin);
	btn_flank_flags[9] = HAL_GPIO_ReadPin(SW9_GPIO_Port,SW9_Pin);
	btn_flank_flags[10] = HAL_GPIO_ReadPin(SW10_GPIO_Port,SW10_Pin);
	btn_flank_flags[11] = HAL_GPIO_ReadPin(SW11_GPIO_Port,SW11_Pin);
}

void vcp_send_switch(uint8_t switchNr)
{
	char buffer[3] = "";
	sprintf(buffer,"s%02d",switchNr);
	CDC_Transmit_FS((uint8_t*)buffer,3);
}
/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */

  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     tex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
