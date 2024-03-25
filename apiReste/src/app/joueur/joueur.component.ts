import { Component, OnInit } from '@angular/core';

import { FormsModule } from "@angular/forms";
import { CommonModule } from '@angular/common';
import { ServicesComponent } from '../services/services.component'; 

@Component({
  selector: 'app-joueur',
  templateUrl: './joueur.component.html',
  imports: [CommonModule, FormsModule],
  standalone: true,
  styleUrls: ['./joueur.component.css']
})

export class JoueurComponent implements OnInit {
  joueurs: any = [];
  nouveauJoueur: any = {};

  constructor(private ServicesComponent: ServicesComponent) {}

  ngOnInit() {
    this.loadJoueur();
  }

  onSubmit() {
    this.saveJoueur(this.nouveauJoueur);
  }

  loadJoueur() {
    this.ServicesComponent.getJoueur().subscribe({
      next: (joueurs: any) => {
        this.joueurs = joueurs;
        console.log('Joueur fetch avec succes', joueurs);
      },
      error: (error) => console.log('erreur de fetch', error)
    });
  }

  saveJoueur(newJoueur: any) {
    this.ServicesComponent.saveJoueur(newJoueur).subscribe({
      next: () => {
        console.log('Joueur ajouté avec succès');
        this.loadJoueur();
      },
      error: (error) => console.log('Erreur lors de l\'ajout du joueur', error)
    });
  }

}
