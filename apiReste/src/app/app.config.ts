import { Routes, RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
export const routes: Routes = [
];
import { JoueurComponent } from './joueur/joueur.component';

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})

export class AppRoutingModule { }

import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';


import { provideClientHydration } from '@angular/platform-browser';
import {provideHttpClient} from "@angular/common/http";

export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes), provideHttpClient()]
};