---
# Leave the homepage title empty to use the site title
title: ""
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: "3rem"

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: ""
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
    design:
      css_class: dark
      background:
        color: black
        image:
          # Add your image background to `assets/media/`.
          filename: stacked-peaks.svg
          filters:
            brightness: 1.0
          size: cover
          position: center
          parallax: false




#
#
#                        !!!!!! не забывай, что я указываю явно номер коммита в гитхабе, что работали пдф файлы. Если обновлял их, то нужно изменить имя коммита тут!!!! Ну или разглдит nbviewer.org
#
#
#

          
  - block: markdown
    id: notes
    content:
      title: <h1>Main Physics Notes</h1>
      subtitle: ''
      text: |-    


        From approximately 2020 I am studying physics by creating notes which collects all important knowledge of parts of physics that I have touched.
        I have some general ideas, why this approach has prospects and I wrote it <a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/6f1f5a4a0005a06918e136b53f5afdfebdd72103/basic%20physics/idea-of-notes.pdf" target="_blank">here</a> (?!!!).
        There is also an explanation, how I am using them, it is not very typical.
        If you are interested, please read this file before opening my notes.


      
        <h2 id="basic physics notes">Notes on Basic Physics </h2>

        Below are notes on the most important parts of physics and which are a fundamental for any theoretical physicist.

        <div style="line-height: 0.4;"> 



        [An Internal Link](/uploads/basic-physics/mechanics.pdf)


        <ul><li><a  href="https://github.com/YuriHolubeu/yuriholubeu.github.io/blob/main/static/uploads/basic%20physics/%E2%96%A0%20%20mechanics.pdf" target="_blank">mechanics-test-2</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/basic%20physics/%E2%96%A0%20%20mechanics.pdf" target="_blank">mechanics</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/basic%20physics/◊%20%20field%20theory.pdf" target="_blank">field theory</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/basic%20physics/◊%20gravity.pdf" target="_blank">gravity</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/basic%20physics/●%20%20quantum%20mechanics.pdf" target="_blank">quantum mechanics</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/basic%20physics/◘%20quantum%20field%20theory.pdf" target="_blank">quantum field theory</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/basic%20physics/☐%20%20statistical%20physics.pdf" target="_blank">statistical physics</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/basic%20physics/☼%20kinetics.pdf" target="_blank">kinetics</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/basic%20physics/♣%20%20electrodynamics.pdf" target="_blank">electrodynamics</a></li></ul>

        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/basic%20physics/☕%20continuum%20mechanics.pdf" target="_blank">continuum mechanics</a></li></ul>

        
        </div>






    design:
      columns: '1'


























          
  - block: markdown
    id: othernotes
    content:
      title: <h1>Extra Notes</h1>
      subtitle: ''

      text: |-    



        From time to time I study mathematics or some specific fields of physics, and I have created notes abot them.


        <table border="0">
        <tr>
        <td><b style="font-size:30px">Notes on Basic Mathematics </b></td>
        <td><b style="font-size:30px">Notes on Specific Physics</b></td>
        </tr>
        <tr>
        <td>
        
        
        <div style="line-height: 0.4;"> 


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/basic%20mathematics/■%20%20mathematical analysis.pdf" target="_blank">mathematical analysis</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/basic%20mathematics/■%20complex analysis.pdf" target="_blank">complex analysis</a></li></ul>

        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/basic%20mathematics/◊  differential equations.pdf" target="_blank">differential equations</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/basic%20mathematics/◊  partial differential equations.pdf" target="_blank">partial diff. equations</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/basic%20mathematics/◊ oscillations.pdf" target="_blank">oscillations</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/basic%20mathematics/◘ differential geometry.pdf" target="_blank"> differential geometry</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/basic%20mathematics/☐ algebra.pdf" target="_blank">algebra</a></li></ul>
        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/basic%20mathematics/☐ linear algebra.pdf" target="_blank">linear algebra</a></li></ul>

        
        
        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/basic%20mathematics/♣%20%20probability%20theory.pdf" target="_blank">probability theory</a></li></ul>



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Mathematics-Notes/blob/main/special%20mathematics/■ special functions.pdf" target="_blank">special functions</a></li></ul>






        </div>





        </td>
        <td>




        <div style="line-height: 0.4;"> 



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/specific%20physics/special%20field%20and%20gravity%20theories.pdf" target="_blank">special theories</a></li></ul>
        



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/specific%20physics/◊%20cosmology.pdf" target="_blank">cosmology</a></li></ul>



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/specific%20physics/●%20quantum%20information%20theory.pdf" target="_blank">quantum information</a></li></ul>



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/specific%20physics/☐%20thermodynamics.pdf" target="_blank">thermodynamics</a></li></ul>



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/specific%20physics/♣%20magnetism.pdf" target="_blank">magnetism</a></li></ul>


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/specific%20physics/optics.pdf" target="_blank">optics</a></li></ul>
        


        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/specific%20physics/superconductivity.pdf" target="_blank">superconductivity</a></li></ul>
        


        </div>


        
        </td>
        </tr>
        </table>
        
        
































          
  - block: markdown
    id: researchnotes
    content:
      title: <h1>Notes on Research Projects</h1>
      subtitle: ''
      text: |- 

        <h2 id="basic physics notes">Notes on Some Reserach Projects in Physics</h2>
        

        I had several research projects, which didn't lead to articles, but nevertheless I undrestood many methods and many formulas, so I collected them in the notes below. These are not the only my projects, but on them I wos working more than on others. Maybe I'll return to some of them one day.



        <div style="line-height: 0.4;"> 



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/some%20projects/◊%20gravitational%20lensing.pdf" target="_blank">gravitational lensing</a></li></ul>



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/some%20projects/◊%20gravitational%20waves.pdf" target="_blank">gravitational waves</a></li></ul>
        



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/some%20projects/◘%20waveguide%20QED.pdf" target="_blank">waveguide QED</a></li></ul>
        



        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/some%20projects/☐%20electronic%20properties%20of%201D%20and%202D%20materials.pdf" target="_blank">electronic properties of 1D and 2D materials</a></li></ul>
        
        
        

        <ul><li><a  href="https://nbviewer.org/github/YuriHolubeu/Physics-Notes/blob/main/some%20projects/duality%20in%20special%20field%20theories.pdf" target="_blank">duality in special field theories</a></li></ul></li></ul>


        </div>









---


