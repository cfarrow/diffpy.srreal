/*****************************************************************************
*
* diffpy.srreal     by DANSE Diffraction group
*                   Simon J. L. Billinge
*                   (c) 2009 Trustees of the Columbia University
*                   in the City of New York.  All rights reserved.
*
* File coded by:    Pavol Juhas
*
* See AUTHORS.txt for a list of people who contributed.
* See LICENSE.txt for license information.
*
******************************************************************************
*
* Concrete implementations of the abstract PeakProfile class:
*
* class GaussPeakProfile -- registered as "gauss"
*
* $Id$
*
*****************************************************************************/

#include <cmath>

#include <diffpy/srreal/PeakProfile.hpp>
#include <diffpy/ClassRegistry.hpp>
#include <diffpy/mathutils.hpp>

using namespace std;
using diffpy::ClassRegistry;

namespace diffpy {
namespace srreal {

//////////////////////////////////////////////////////////////////////////////
// class PeakProfile
//////////////////////////////////////////////////////////////////////////////

// Constructors --------------------------------------------------------------

PeakProfile::PeakProfile() : mprecision(0.0)
{
    this->registerDoubleAttribute("precision", this,
            &PeakProfile::getPrecision,
            &PeakProfile::setPrecision);
}


// Public Methods ------------------------------------------------------------

void PeakProfile::setPrecision(double eps)
{
    mprecision = eps;
}


const double& PeakProfile::getPrecision() const
{
    return mprecision;
}

// Factory Functions ---------------------------------------------------------

PeakProfile* createPeakProfile(const string& tp)
{
    return ClassRegistry<PeakProfile>::create(tp);
}


bool registerPeakProfile(const PeakProfile& ref)
{
    return ClassRegistry<PeakProfile>::add(ref);
}


bool aliasPeakProfile(const string& tp, const string& al)
{
    return ClassRegistry<PeakProfile>::alias(tp, al);
}


set<string> getPeakProfileTypes()
{
    return ClassRegistry<PeakProfile>::getTypes();
}

}   // namespace srreal
}   // namespace diffpy

// End of file
