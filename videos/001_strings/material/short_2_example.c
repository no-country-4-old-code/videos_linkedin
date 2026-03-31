/*==============================================================================
 * File:        short_2_example.c
 * Project:     Firmware Update Utility v4.2
 * Author:      Embedded Systems Team
 * Target:      IoT Gateway Device
 *
 * Compile:
 *   gcc -o firmware-update-v4.2 short_2_example.c
 *
 * Demo (short_2):
 *   strings -t x firmware-update-v4.2 | grep -Ff common_user_names.txt
 *   xxd -s <offset> -l 0x40 firmware-update-v4.2
 *   echo "cGFzc3dvcmQxMjM=" | base64 -d
 *==============================================================================*/

#include <stdio.h>
#include <string.h>

/*==============================================================================
 * Device configuration — stored in .data section
 *==============================================================================*/
#define FW_VERSION "4.2.1"
#define DEVICE_MODEL "IoT-GW-4200"
#define BUILD_DATE "2024-11-07"

/* Authentication credentials */
static const char fw_username[] = "admin";
static const char fw_auth_key[] = "cGFzc3dvcmQxMjM=";

/*==============================================================================
 * Firmware metadata strings — appear in strings(1) output
 *==============================================================================*/
static const char fw_version[] = "Firmware-Version: " FW_VERSION;
static const char fw_model[] = "Device-Model: " DEVICE_MODEL;
static const char fw_build[] = "Build-Date: " BUILD_DATE;
static const char fw_boot_msg[] = "System Boot OK";
static const char fw_update_url[] =
    "https://updates.iot-gw.internal/v4/firmware";
static const char fw_api_token[] =
    "X-Update-Token: Ym90c2VjcmV0dG9rZW4="; /* base64 */
static const char fw_copyright[] =
    "Copyright (c) 2024 IoT Systems GmbH. All rights reserved.";

/*==============================================================================
 * Main — this is a firmware update stub, not a running daemon
 *==============================================================================*/
int main(void) {
  /* Simulate firmware update initialization */
  printf("[%s] Firmware Update Utility v%s\n", DEVICE_MODEL, FW_VERSION);
  printf("[%s] Build: %s\n", DEVICE_MODEL, BUILD_DATE);
  printf("[%s] %s\n", DEVICE_MODEL, fw_boot_msg);

  /* Authenticate against update server */

  printf("[update] Connecting to %s\n", fw_update_url);
  printf("[update] Done.\n");

  return 0;
}
