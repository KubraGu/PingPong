import { Component } from '@angular/core';
import {inject, Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";


@Injectable({
  providedIn: 'root'
})

export class ServicesComponent {
  private  http = inject(HttpClient);
  constructor() { }
  getJoueur(){
      return this.http.get("/api/joueur");
  }
  saveJoueur(joueur: any) {
    return this.http.post("/api/joueur", joueur);
  }
}
