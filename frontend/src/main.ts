// frontend/src/main.ts

import { registerLocaleData } from '@angular/common';
import localeTr from '@angular/common/locales/tr'; 

import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
// Lütfen kendi AppComponent import'unuzu kontrol edin (bu örnekteki yol varsayımsaldır)
import { AppComponent } from './app/app'; 

// KRİTİK İŞLEM: Türkçe (tr) yerel ayarını Angular'a resmi olarak kaydediyoruz.
registerLocaleData(localeTr, 'tr'); 


bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));